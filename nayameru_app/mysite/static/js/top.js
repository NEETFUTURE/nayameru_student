+$(function(){
  'use strict';

  let AddFlg = 0;
  let AddOther = () =>{
    let text = document.getElementById("text").value;
    let pub = document.getElementById("pub").value;
    if (AddFlg===0){
      document.getElementById("allText").value += text + pub;
      AddFlg = 1;
    } else {
      document.getElementById("allText").value += "," + text + pub;
    }
  }

  let RemoveInput = ()=>{
    document.getElementById("text").value = "";
    document.getElementById("pub").value = "";
    if(document.getElementById("alert-text")){
      document.getElementById("alert").removeChild(document.getElementById("alert-text"));
    }
  }

  //出版社のみの入力に対し警告を出す関数
  let SmartAlert = () =>{
    if(document.getElementById("alert-text") != null) return false;
    $('#alert').append("<div id='alert-text' class='alert alert-danger' role='alert'><span class='glyphicon glyphicon-exclamation-sign' aria-hidden='true'></span><span class='sr-only'>Error:</span> 出版社のみの入力はできません。</div>");
  }

  let Check = () =>{
    let text = document.getElementById("text").value;
    let pub = document.getElementById("pub").value;
    if((!pub.match(/\S/g) && !text.match(/\S/g)) || !text.match(/\S/g)){
      console.log("出版社のみの入力は不正だと");
      let width = $(window).width();
      RemoveInput();
      SmartAlert();
    } else {
      AddOther();
      RemoveInput();
    }
  }

  let PushEnter = (e) =>{
    let key = e.which || e.keycode;
    if(key === 13){
      document.getElementById("btn").click();
    }
  }

  let Search = (e) =>{
    let key = e.which || e.keycode;
    if(key === 13){
      document.getElementById("s-btn").click();
    }
  }
  document.getElementById("btn").addEventListener('click', Check, false);
  document.getElementById("allText").addEventListener('keypress', Search, false);
  document.getElementById("text").addEventListener('keypress', PushEnter, false);
  document.getElementById("pub").addEventListener('keypress', PushEnter, false);;


})
