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



fetch('http://127.0.0.1:8000/items/').then((data) => {
  return data.json();
}).then((completeData) => {

  let data1 = "";
  counter = 0
  const parent_element = document.querySelector('[target=""]');

  let row = document.createElement('div');
  row.setAttribute("class", "row justify-content-center");

  completeData.map((data) => {
    imgUrl = 'data:image/png;base64,' + data.images
    data1 += `<div class="card mb-7">
        <img src=${imgUrl} class="card-img-top" alt="...">
        <div class="card-body px-0">
            <div class="fs-xs"><a href="#" class="text-muted">${data.category}</a></div>
            <div class="fw-bold"><a href="#" class="text-body">${data.name}</a></div>
            <div class="btn-cont">
                          <div class="fw-bold text-muted">${data.price}</div>
                        <a href="#" id="btn" class="btn btn-primary">Виж продукт</a>
                      </div>
          </div>
        </div>`

    row.innerHTML = data1;
    counter++;
    if (counter === 4) {
      parent_element.appendChild(row)
      parent_element.appendChild(document.createElement('br'));
      row = document.createElement('div');
      row.setAttribute("class", "row justify-content-center");
      row.setAttribute("target", "");
      data1 = ""
    }
  });
  parent_element.appendChild(row)
  parent_element.appendChild(document.createElement('br'));

}).catch((err) => {
  console.log(err);
});




const card = document.querySelector('.subscribe-card');
document.querySelector('.form').addEventListener('submit', function (e) {
  e.preventDefault();
  card.classList.add('done');
});

/*SUB CARD*/
const sub_card = document.querySelector('.sub-card');
document.querySelector('.form').addEventListener('submit', function(e) {
  e.preventDefault();
  sub_card.classList.add('done');
});
