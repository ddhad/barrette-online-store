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
const secondaryImgs = document.querySelector(".d-flex.justify-content-center.mb-3");

document.addEventListener('DOMContentLoaded', function () {
  console.log(secondaryImgs)
  mainImg.setAttribute("src", "data:image/png;base64," + productImgs[1]);
  let data = "";
  productImgs.forEach((imgSrc) => {
    let imgEl = document.createElement("a");
    imgEl.setAttribute("data-fslightbox", "mygalley");

    data += `<a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
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
  const mainImg = document.getElementById("imageBox");
  mainImg.src = smallImg.src;
}


// fetch('http://127.0.0.1:8000/item/1').then((data) => {
//   return data.json();
// }).then((completeData)=> {
//   let product1 = "";
//   const parent_el = document.querySelector(".row.gx-5");

//   let aside = document.createElement("aside");
//   aside.setAttribute("class", "col-lg-6");


//   completeData.map((data) => {
//     console.log(data)
//   //   console.log(data.images)
//   //   // for (i = 0; i < data.images.length; i++) {
//   //   //   imgUrl = "data:image/png;base64," + data.images[i];
//   //   //   console.log(imgUrl);

//     // }

//     product1 += `<div class="border rounded-4 mb-3 d-flex justify-content-center">
//     <a data-fslightbox="mygalley" class="rounded-4" target="_blank" data-type="image">
//       <img style="max-width: 100%; max-height: 60vh; margin: auto;" id="imageBox" class="rounded-4 fit"
//         src="Images/1-9642666.png" />
//     </a>
//   </div>
//   <div class="d-flex justify-content-center mb-3">
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" id="imageBox" class="rounded-4 fit" src=${imgUrl}
//         onclick="myFunction(this)" />
//     </a>
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" class="rounded-2" src="/Images/7-9642665.jpg" onclick="myFunction(this)" />
//     </a>
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" class="rounded-2" src="/Images/2-9642666.png" onclick="myFunction(this)" />
//     </a>
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" class="rounded-2" src="/Images/3-9642667.png" onclick="myFunction(this)" />
//     </a>
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" class="rounded-2" src="/Images/5-9642663.jpg" onclick="myFunction(this)" />
//     </a>
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" class="rounded-2" src="/Images/4-9642663.jpg" onclick="myFunction(this)" />
//     </a>
//     <a data-fslightbox="mygalley" class="border mx-1 rounded-2" target="_blank" data-type="image"
//       class="item-thumb">
//       <img width="60" height="60" class="rounded-2" src="/Images/6-9642664.jpg" onclick="myFunction(this)" />
//     </a>
//   </div>`
//   })
// })










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