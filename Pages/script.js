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
