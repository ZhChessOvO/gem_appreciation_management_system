window.onload = function () {
			let table = document.getElementById("table");
			let btn = document.getElementsByClassName("button");
			let row = table.rows.length;
			let col = table.rows.item(0).cells.length;
			let flag = true;

			for(let i = 0; i< btn.length; i++) {
				btn[i].addEventListener("click",function(e) {
					//默认升序排列
					if(flag == true) {
						for(let j = 0;j<row-1;j++){
							for(let z = 0;z<row-j-1;z++){
								if(table.rows[z].cells[i].innerHTML > table.rows[z+1].cells[i].innerHTML){
									for(let k = 0;k<col;k++){
										let temp = table.rows[z].cells[k].innerHTML;
										table.rows[z].cells[k].innerHTML = table.rows[z+1].cells[k].innerHTML;
										table.rows[z+1].cells[k].innerHTML = temp;
									}
								}
							}
						}
					}
					else{
						for(let j = 0;j<row-1;j++){
							for(let z = 0;z<row-j-1;z++){
								if(table.rows[z].cells[i].innerHTML < table.rows[z+1].cells[i].innerHTML){
									for(let k = 0;k<col;k++){
										let temp = table.rows[z].cells[k].innerHTML;
										table.rows[z].cells[k].innerHTML = table.rows[z+1].cells[k].innerHTML;
										table.rows[z+1].cells[k].innerHTML = temp;
									}
								}
							}
						}
					}
					flag = false;
				});
			}
		}