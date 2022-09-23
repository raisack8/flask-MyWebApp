const myHeading = document.querySelector('h1');

const iTest = 12;
if(iTest%2===0){
    myHeading.textContent = `${iTest}は偶数です`;
}else{
    myHeading.textContent = `${iTest}は奇数です`;
}
const myDiv = document.querySelector('div');


// alert(myDiv.textContent);

// 2つの引数の乗算の関数
function multiply(num1,num2) {
    let result = num1 * num2;
    return result;
  }

  // divをクリックしたらMsgBox
  // クリックイベント
  document.querySelector('html').addEventListener('click', function () {
    alert('痛っ! つつかないで!');
  });
  // documentをクエリ選択して、そこにメソッド的に処理を追加していく
