//全局变量
        var numCount;       //数据总数量
        var columnsCounts;  //数据列数量
        var pageCount;      //每页显示的数量
        var pageNum=1;        //总页数
        var currPageNum ;   //当前页数

        //页面标签变量
        var blockTable;
        var preSpan;
        var firstSpan;
        var nextSpan;
        var lastSpan;
        var pageNumSpan;
        var currPageSpan;

		function prePage(){
		    hide();
		    currPageNum--;
		    showCurrPage(currPageNum);
		    showTotalPage();
		    var firstR = firstRow(currPageNum);
		    var lastR = lastRow(firstR);
		    for(i = firstR; i < lastR; i++){
		        blockTable.rows[i].style.display = "";
		    }

		    if(1 == currPageNum){
		        firstText();
		        preText();
		        nextLink();
		        lastLink();
		    }else if(pageNum == currPageNum){
		        preLink();
		        firstLink();
		        nextText();
		        lastText();
		    }else{
		        firstLink();
		        preLink();
		        nextLink();
		        lastLink();
		    }

		}

		function nextPage(){
		    hide();
		    currPageNum++;
		    showCurrPage(currPageNum);
		    showTotalPage();
		    var firstR = firstRow(currPageNum);
		    var lastR = lastRow(firstR);
		    for(i = firstR; i < lastR; i ++){
		        blockTable.rows[i].style.display = "";
		    }

		    if(1 == currPageNum){
		        firstText();
		        preText();
		        nextLink();
		        lastLink();
		    }else if(pageNum == currPageNum){
		        preLink();
		        firstLink();
		        nextText();
		        lastText();
		    }else{
		        firstLink();
		        preLink();
		        nextLink();
		        lastLink();
		    }
		}

		function lastPage(){
		    hide();
		    currPageNum = pageNum;
		    showCurrPage(currPageNum);
		    showTotalPage();
		    var firstR = firstRow(currPageNum);
		    for(i = firstR; i < numCount + 1; i++){
		        blockTable.rows[i].style.display = "";
		    }

		    firstLink();
		    preLink();
		    nextText();
		    lastText();
		}

		// 计算将要显示的页面的首行和尾行
		function firstRow(currPageNum){
		    return pageCount*(currPageNum - 1) + 1;
		}
		//计算尾行
		function lastRow(firstRow){
		    var lastRow = firstRow + pageCount;
		    //如果到了最后一页不足则单独计算
		    if(lastRow > numCount + 1){
		        lastRow = numCount + 1;
		    }
		    return lastRow;
		}

		function showCurrPage(cpn){
		    currPageSpan.innerHTML = cpn;
		}

		function showTotalPage(){
		    pageNumSpan.innerHTML = pageNum;
		}

		window.onload=function(){
			//页面标签变量
            blockTable = document.getElementById("blocks");
            preSpan = document.getElementById("spanPre");
            firstSpan = document.getElementById("spanFirst");
            nextSpan = document.getElementById("spanNext");
            lastSpan = document.getElementById("spanLast");
            pageNumSpan = document.getElementById("spanTotalPage");
            currPageSpan = document.getElementById("spanPageNum");

            numCount = document.getElementById("blocks").rows.length-1;
            //取table的行数作为数据总数量（减去标题行1）
            alert(numCount)
            columnsCounts = blockTable.rows[0].cells.length;
            pageCount = 2;
            pageNum = parseInt(numCount/pageCount);

            var temp=numCount;
            //计算一共有多少页
            while(0 != temp%pageCount)
            {
                pageNum += 1;
                temp/=pageCount;
            }

		}