// 文字列Bが文字列Aの部分文字列かどうか返す
function subString(A, B){
  let j = 0;
  for(let i = 0; i < A.length; i ++){
    if(A[i].toUpperCase() === B[j].toUpperCase()){
      j ++;
      if(j == B.length){
        return true;
      }
    }
  }
  return false;
}

const form = document.querySelector("#form1");
const input = document.querySelector("#baba-input");
const resBlock = document.querySelector("#result-block");

form.addEventListener("submit", (e) => {
  //submitで発火
  e.preventDefault(); //送信しない
  resBlock.innerHTML = "";
  let aisu = input.value;
  if(aisu.length > 100000) location.href = "https://twitter.com/3_3_nk/status/1033066522439081985";
  if(aisu == "aisu") location.href = "https://twitter.com/aisu_uu/status/1294125344652324864";
  let aisuText = "<p>" + aisu + "</p>";
  resBlock.insertAdjacentHTML("afterbegin", aisuText);
  let aisuSort = aisu.toUpperCase().split('').sort();
  for (const [key, value] of Object.entries(obj_name_data)) {
    if (subString(aisuSort, value["sorted_name"])) {
      let img = '<img src="' + value['img'] + '" />';
      resBlock.insertAdjacentHTML("beforeend", "<p>" + img + " " + key + "</p>");
    }
  }
});
