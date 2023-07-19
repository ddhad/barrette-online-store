const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}))


/*Image converter*/
const productImgs = JSON.parse(document.getElementById('productImages').dataset.productImages);
const mainImg = document.getElementById("imageBox");
const secondaryImgs = document.getElementById("secondaryImageBox");

document.addEventListener('DOMContentLoaded', function () {
  console.log(secondaryImgs)
  console.log(mainImg)
  mainImg.setAttribute("src", "data:image/png;base64," + productImgs[0]);
  let data = "";
  productImgs.forEach((imgSrc) => {
    let imgEl = document.createElement("a");
    imgEl.setAttribute("data-fslightbox", "mygalley");

    data = `<a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
    class="item-thumb">
    <img width="60" height="60"  class="rounded-4 fit" src="data:image/png;base64,${imgSrc}"
      onclick="selectImg(this)"/>
    </a>`
    imgEl.innerHTML = data;
    secondaryImgs.appendChild(imgEl);
  });
  
});


/*Image Slider*/
function selectImg(smallImg) {
  mainImg.src = smallImg.src;
}


/*QUANTITY*/
const plus = document.querySelector("#button-addon2"),
  minus = document.querySelector("#button-addon1"),
  num = document.querySelector(".form-control");
let a = 1;

plus.addEventListener("click", () => {
  a++;
  num.innerHTML = a;
})

minus.addEventListener("click", () => {
  if (a > 1) {
    a--;
    num.innerHTML = a;
  }
})

/*SUB CARD(FOOTER)*/
const sub_card = document.querySelector('.sub-card');
document.querySelector('.form').addEventListener('submit', function (e) {
  e.preventDefault();
  sub_card.classList.add('done');
});