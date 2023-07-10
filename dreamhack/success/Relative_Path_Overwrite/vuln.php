<script src="filter.js"></script>
<!-- 그러니깐 결국에는 filter.js를 못 가져오게 하면 위 조건문을 검사하지 않아도 됨. -->
<pre id=param></pre>
<script>
    var param_elem = document.getElementById("param");
    var url = new URL(window.location.href); // window.location.href는 현재 url을 가지고 오는거다.
    var param = url.searchParams.get("param");
    if (typeof filter !== 'undefined') { // 만약 filter가 undefined라면 이 조건문을 검사하지 않음.
        for (var i = 0; i < filter.length; i++) {
            if (param.toLowerCase().includes(filter[i])) {
                param = "nope !!";
                break;
            }
        }
    }
    param_elem.innerHTML = param; // innerHTML로 렌더링되는 경우, 브라우저는 스크립트 태그를 실행하지 않습니다. 그러나 <img> 태그의 onerror 속성과 같은 이벤트 속성은 웹 페이지가 로드될 때 실행되므로 공격이 가능합니다.
</script>
