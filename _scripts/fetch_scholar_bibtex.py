import os
import time
from pathlib import Path

try:
    from scholarly import scholarly, ProxyGenerator
except Exception as exc:
    raise SystemExit("scholarly is not installed. Run: pip install scholarly") from exc


SCHOLAR_ID = "ivTfnKgAAAAJ"


def init_proxy() -> None:
    """Try to set up a proxy to reduce blocking. Falls back silently."""
    try:
        pg = ProxyGenerator()
        # Try free proxies first; this is best-effort and may fail silently
        if pg.FreeProxies():
            scholarly.use_proxy(pg)
            return
    except Exception:
        pass


def fetch_bibtex_entries(scholar_user_id: str, max_pubs: int | None = None) -> list[str]:
    author = scholarly.search_author_id(scholar_user_id)
    author = scholarly.fill(author, sections=["publications"])  # type: ignore[arg-type]

    entries: list[str] = []
    publications = author.get("publications", [])  # type: ignore[assignment]
    for idx, pub in enumerate(publications):
        try:
            pub = scholarly.fill(pub)
            bibtex = scholarly.bibtex(pub)
            if bibtex:
                entries.append(str(bibtex).strip())
        except Exception:
            # Skip entries that fail to fetch (rate limits/CAPTCHA/etc.)
            pass
        # Be polite to Google Scholar to reduce rate limit/CAPTCHA
        time.sleep(0.8)
        if max_pubs is not None and idx + 1 >= max_pubs:
            break
    return entries


def write_bibtex_file(entries: list[str], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        # Keep Jekyll-style front matter as in the template repo
        f.write("---\n---\n\n")
        f.write("\n\n".join(entries))
        f.write("\n")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    out_file = repo_root / "_bibliography" / "papers.bib"
    init_proxy()
    entries = fetch_bibtex_entries(SCHOLAR_ID)
    if not entries:
        raise SystemExit("No entries fetched from Google Scholar. Try again later or add manually.")
    write_bibtex_file(entries, out_file)
    print(f"Wrote {len(entries)} entries to {out_file}")


if __name__ == "__main__":
    main()

