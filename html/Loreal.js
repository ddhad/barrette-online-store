//HEADER
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link-main").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}))
//HEADER








//FOOTER
const sub_card = document.querySelector('.sub-card');
document.querySelector('.form').addEventListener('submit', function (e) {
  e.preventDefault();
  sub_card.classList.add('done');
});
//FOOTER
