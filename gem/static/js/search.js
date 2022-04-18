function getInputVal(){
			const inputBox = document.querySelectorAll('.input-box')[0],
				  content = document.querySelectorAll('.content')[0];
			// 获取input输入框中的值
			let inputVal = inputBox.value;
			content.innerHTML = inputVal;
}

window.onload = function () {
			var table = document.getElementById("table");
			var btn = document.getElementsByClassName("button");
			var row = table.rows.length;
			var col = table.rows.item(0).cells.length;
			var flag = true;


			for(var i = 0; i< btn.length; i++) {
				bth[i].addEventListener("click",function(e) {
					for(var j=0;j<btn.length;j++){
						if(table.rows[j].cells[i].innerHTML==inputVal){
							console.log(table.rows[j].cells[i].innerHTML);
						}
					}

		});
	}
}