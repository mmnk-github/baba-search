const xmlht = new XMLHttpRequest();
let obj_name_data;
xmlht.open('get', './obj_name_data.json', false);
xmlht.onload = function(){
  try{
    obj_name_data = JSON.parse(this.responseText);
  }catch(e){
    alert("読み込み失敗");
  }
}
xmlht.send(null);

console.log(obj_name_data);

// 変わる
const babaNames = ["fofo", "baba"]; // 配列(順序アリ)
const imgObj = {
    fofo: "./image/FOFO.gif",
    baba: "./image/BABA.gif"
}; // オブジェクト(順序なし)
// オブジェクト名: "画像ファイルへのパス"

const form = document.querySelector("#form1");
const input = document.querySelector("#baba-input");
const resBlock = document.querySelector("#result-block");

form.addEventListener("submit", (e) => {
  console.log(obj_name_data);
  //submitで発火
  e.preventDefault(); //送信しない
  resBlock.innerHTML = "";
  let aisu = input.value;
  let aisuText = "<p>" + aisu + "</p>";
  resBlock.insertAdjacentHTML("afterbegin", aisuText);
  // カエルゲロゲロ🐸
  for (const [key, value] of Object.entries(imgObj)) {
    const re = new RegExp(key);
    if (aisu.toLowerCase().match(re)) {
      console.log("found");
      let img = '<img src="' + value + '" />';
      resBlock.insertAdjacentHTML("beforeend", img);
    } else {
      console.log("not found");
    }
  }

});
