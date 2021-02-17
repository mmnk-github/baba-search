// 文字列Bが文字列Aの部分文字列かどうか返す
function subString(A, B){
  let j = 0;
  for(let i = 0; i < A.length; i ++){
    if(B == 'IMAGE'){
      console.log(i, j);
    }
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
  let aisuText = "<p>" + aisu + "</p>";
  resBlock.insertAdjacentHTML("afterbegin", aisuText);
  let aisuSort = aisu.split('').sort();
  for (const [key, value] of Object.entries(obj_name_data)) {
    if (subString(aisuSort, value["sorted_name"])) {
      let img = '<img src="' + value['img'] + '" />';
      resBlock.insertAdjacentHTML("beforeend", "<p>" + img + key + "</p>");
    }else{
      console.log("unko");
    }
  }
});
