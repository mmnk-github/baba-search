// 変わる
const babaNames = ["fofo", "baba"]; // 配列(順序アリ)
const imgObj = {
    fofo: "./image/fofo_27_1.png",
    baba: "hogehoge"
}; // オブジェクト(順序なし)
// オブジェクト名: "画像ファイルへのパス"

const form = document.querySelector("#form1");
const input = document.querySelector("#aisu");
const resBlock = document.querySelector("#resultBlock");

form.addEventListener("submit", (e) => {
    //submitで発火
    e.preventDefault(); //送信しない
    resBlock.innerHTML = "";
    let aisu = input.value;
    let aisuText = "<p>" + aisu + "</p>";
    resBlock.insertAdjacentHTML("afterbegin", aisuText);
    // カエルゲロゲロ🐸
    if (aisu.toLowerCase().match(/fofo/)) {
        console.log("found");
        let img = '<img src="' + imgObj.fofo + '" />'
        resBlock.insertAdjacentHTML("beforeend", img);
    } else {
        console.log("not found");
    }
});