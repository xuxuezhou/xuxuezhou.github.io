---
layout: sections
title: More about me
permalink: /more-about-me/
nav: false
sections:
  - id: hobbies
    title: Hobbies
  - id: proposals
    title: Proposals
  - id: tools
    title: Tools
  - id: photos
    title: Photos
---

<section class="home-section" id="hobbies">
  <h2 class="section-heading">Hobbies</h2>
  <p>
    <strong class="hobby-badminton">Badminton.</strong> I love playing badminton. I won the team gold medal at the Shaoxing Badminton
    Championships and reached the top four in both singles and doubles. My favorite players are Shi Yuqi and Kento
    Momota. If you'd like to play a game together, feel free to <a id="WeChatBtn" href="javascript:void(0)" title="WeChat">reach out on WeChat</a>!
  </p>
  <p>
    <strong class="hobby-photography">Photography.</strong> I like observing the world through photography, especially street photography and
    nature landscapes.
  </p>
  <p>
    <strong class="hobby-calligraphy">Calligraphy.</strong> I practice Chinese calligraphy. I have studied Zhiyong's <em>Thousand Character
    Classic</em> (智永《千字文》), Wang Xizhi's <em>Preface to the Orchid Pavilion Collection</em> (《兰亭序》) and Yan
    Zhenqing's <em>Draft of a Requiem to My Nephew</em> (《祭侄文稿》). My favorite calligrapher is Su Shi
    (Su Dongpo, 苏轼), especially his <em>Cold Food Observance in Huangzhou</em> (《黄州寒食诗帖》). I love his grand,
    free-spirited style with bold, expressive ink.
  </p>
  <p>To me, badminton and calligraphy have something in common: both are full of rhythm (韵律).</p>
</section>

<hr>

<section class="home-section" id="proposals">
  <h2 class="section-heading">Proposals</h2>
  <p>
    I'm working on proposals in several directions. Feel free to
    <a href="mailto:{{ site.data.socials.email | encode_email }}">contact me</a>
    if you'd be interested in learning more!
  </p>
  <ol class="proposal-list">
    <li>Brain-Body Co-evolving System towards AGI</li>
  </ol>
</section>

<hr>

<section class="home-section" id="tools">
  <h2 class="section-heading">Tools</h2>
  <p>Some open-source tools I built in my spare time with vibe coding.</p>
  <ul class="tool-list">
    <li>
      <a class="tool-name" href="https://github.com/xuxuezhou/plume-studio">Plume Studio</a>
      — a writing workspace that runs entirely in the browser: block editor, image layouts and version history, with no account or server needed.
      <span class="tool-links"><a href="https://xuxuezhou.github.io/plume-studio/">try it</a> | <a href="https://github.com/xuxuezhou/plume-studio">github</a></span>
    </li>
    <li>
      <a class="tool-name" href="https://github.com/xuxuezhou/scorespace">ScoreSpace</a>
      — turns photos or PDFs of guitar and piano sheet music into digital scores, with follow-along highlighting, auto page-turning and a virtual keyboard/fretboard. Web and iOS.
      <span class="tool-links"><a href="https://xuxuezhou.github.io/scorespace/">try it</a> | <a href="https://github.com/xuxuezhou/scorespace">github</a></span>
    </li>
  </ul>
</section>

<hr>

<section class="home-section" id="photos">
  <h2 class="section-heading">Photos</h2>
  <p class="blogs-empty">Coming soon.</p>
</section>

<!-- WeChat QR popup (opened by the "reach out on WeChat" link above) -->
<div id="WeChatMod" class="wechat-modal">
  <img src="{{ site.data.socials.wechat_qr | prepend: 'assets/img/' | relative_url }}" alt="WeChat QR" id="WeChatQR">
</div>
<script defer src="{{ '/assets/js/wechat.js' | relative_url | bust_file_cache }}" type="text/javascript"></script>
