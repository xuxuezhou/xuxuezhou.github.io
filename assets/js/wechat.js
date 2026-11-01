var wechatModal = document.getElementById("WeChatMod");
// Move the modal to <body> so it is not clipped by sticky/stacked parents (e.g. the profile sidebar).
if (wechatModal && wechatModal.parentNode !== document.body) {
  document.body.appendChild(wechatModal);
}
var wechatBtn = document.querySelectorAll('[id="WeChatBtn"]');

for (var i = 0; i < wechatBtn.length; i++) {
  wechatBtn[i].onclick = function () {
    wechatModal.style.display = "block";
  };
}

window.onclick = function (event) {
  if (event.target == wechatModal) {
    wechatModal.style.display = "none";
  }
};
