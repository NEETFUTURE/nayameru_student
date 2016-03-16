+$(function(){
  'use strict';

  let AddOther = () =>{
    let text = document.getElementById("text").value;
    let pub = document.getElementById("pub").value;
    console.log(text+pub)
    document.getElementById("mybox").value = text + pub;

  }

  let fuga = () =>{
    let pub = document.getElementById("pub").value;
    //console.log(text);
    if(!pub.match(/\S/g)){
      console.log("出版社のみの入力は不正だと");
    } else {
      console.log("hello");
      AddOther();
    }
  }

  let button = document.getElementById("btn");
  button.addEventListener('click', fuga, false);


})
