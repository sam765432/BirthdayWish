
let i = 0;
let text1 = "Hey! Kuhu(Aadya).";
let text2 = "Today is the your Birthday."
let speed = 100;

function typeWriter(text, para){
	if(ok == 2){
		clearInterval(typeInterval);
	}
	if(i < text.length){
		document.getElementById(para).innerHTML += text.charAt(i);
		i++;
		speed = Math.random() * 50 + 100;
	}
	else{
		if(ok == 0){
			i = 0;
		}
		ok += 1;
	}
}

var typeInterval;

//window.onload = function() {
//	window.onload = function(){};
   	typeInterval = setInterval(function(){
		if(ok == 0){
			typeWriter("Hey! Kuhu(Aadya).", "txt1");
		}
		else if(ok == 1){
			typeWriter("Today is the your Birthday.", "txt2");
		}
	}, 100);
//};
