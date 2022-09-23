class Initialize {
    constructor() {
        const myHeading = document.querySelector('h1');
        myHeading.textContent = 'Init';
    }
}

const init = new Initialize();

const iTest = 12;
// if(iTest%2===0){
//     myHeading.textContent = `${iTest}は偶数です`;
// }else{
//     myHeading.textContent = `${iTest}は奇数です`;
// }
const myDiv = document.querySelector('div');


// alert(myDiv.textContent);

// 2つの引数の乗算の関数
function multiply(num1,num2) {
    let result = num1 * num2;
    return result;
  }

// divをクリックしたらMsgBox
// クリックイベント

//   document.querySelector('html').addEventListener('click', function () {
//     alert('痛っ! つつかないで!');
//   });

// documentをクエリ選択して、そこにメソッド的に処理を追加していく
// let で変数にdocument.querySelector('html')を格納して
// そこにアドイベントをつけるのもよし。

//   const myImage = document.querySelector('img');

//   myImage.onclick = () => {
//     const mySrc = myImage.getAttribute('src');
//     if (mySrc === 'resource/arrow.png') {
//       myImage.setAttribute('src','resource/dcg.png');
//     } else {
//       myImage.setAttribute('src','resource/arrow.png');
//     }
//   }


let i = 0;
const imgObj=  document.querySelector('img');
const myHeading = document.querySelector('h1');
imgObj.addEventListener('click', function () {
    const mySrc = imgObj.getAttribute('src');
    if (mySrc === 'resource/arrow.png') {
        imgObj.setAttribute('src','resource/dcg.png');
        myDiv.textContent=`resource/dcg.png_${i}`;
    } else {
        imgObj.setAttribute('src','resource/arrow.png');
        myDiv.textContent=`resource/arrow.png_${i}`;
    }
    i = Incremant(i);
    myHeading.textContent = i;
});

function Incremant(i){
    let addedInt = i + 1;
    if(addedInt>5){
        addedInt = 0;
    }
    return addedInt
}


function setUserName() {
    const myName = prompt('あなたの名前を入力してください。');

    if(!myName)
    {
        setUserName();
    }
    else
    {
        localStorage.setItem('name', myName);
        myHeading.textContent = `Mozilla はかっこいいよ、${myName}`;
    }
}

// 上のボタン入力で入力したデータを保存しておく
if (!localStorage.getItem('name')) {
    setUserName();
} 
else 
{
    const storedName = localStorage.getItem('name');
    myHeading.textContent = `Mozilla はかっこいいよ、${storedName}`;
}

const btnOgj = document.querySelector('button');
btnOgj.onclick = () => {
    setUserName();
}