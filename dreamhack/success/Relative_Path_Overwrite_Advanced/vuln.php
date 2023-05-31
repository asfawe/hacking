<script src="filter.js"></script> 
<pre id=param></pre>
<script>
    var param_elem = document.getElementById("param");
    var url = new URL(window.location.href);
    var param = url.searchParams.get("param");
	
    if (typeof filter === 'undefined') {
        param = "nope !!"; 
    }
    else {
        for (var i = 0; i < filter.length; i++) {
            if (param.toLowerCase().includes(filter[i])) {
                param = "nope !!";
                break;
            }
        }
    }

    param_elem.innerHTML = param;
</script>

<!-- filter.js를 true로 만들고 base-uri를 이용해서 뚫으면 될 듯?? 근데 그거는 불가능.... 위에 스크립트 먼저 들어감... -->