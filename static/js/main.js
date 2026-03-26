// ---------------------------------------
// ローディング
// ---------------------------------------

window.addEventListener("load", function () {
  const loading = document.getElementById("loading");
  loading.style.display = "none";
});


// ---------------------------------------
// ユーザ側
// ---------------------------------------

// 商品絞り込み
function filterSeries(series) {
  const products = document.querySelectorAll(".productWrapper");
  products.forEach((p) => {
    if (series === "All" || p.dataset.series === series) {
      p.style.display = "block";
    } else {
      p.style.display = "none";
    }
  });
}
function filterColor(color) {
  const products = document.querySelectorAll(".productWrapper");
  products.forEach((p) => {
    if (p.dataset.color === color) {
      p.style.display = "block";
    } else {
      p.style.display = "none";
    }
  });
}

// 検索ボックス
function toggleInvisible() {
  const searchBox = document.querySelector(".searchBox");
  searchBox.classList.toggle("show");
}


// ---------------------------------------
// 管理者側
// ---------------------------------------

// 登録商品画像プレビュー
const imgFile = document.getElementById("img_file");
if(imgFile){
  imgFile.addEventListener("change", function(e){
    const file = e.target.files[0]
    if(file){
      const reader = new FileReader()
      reader.onload = function(event){
        const preview = document.getElementById("img_preview");
        preview.src = event.target.result
        preview.style.display="block";

        const current = document.getElementById("current_img")    
        if(current){
          current.style.display="none";
        }
      }
      reader.readAsDataURL(file)
    }
  })
}

// 注文情報絞り込み
function filterProsessing(processing) {
  const orders = document.querySelectorAll(".adminOrder");
  orders.forEach((o) => {
    if (processing === "All" || o.dataset.processing === String(processing)) {
      o.style.display = "table-row";
    } else {
      o.style.display = "none";
    }
  });
}
