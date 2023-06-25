function sum(a, b) {
	return a + b;
}

const promise = new Promise((resolve, reject) => {
	setTimeout(() => {
	  resolve(sum(1,1)); // 이행 상태로 전환하고 결과 값을 전달
	}, 1000);
  });

promise.then((result) => {
// 작업이 성공적으로 완료된 경우 호출되는 콜백 함수
console.log(result); // "작업 완료!" 출력
return result + 1;
}).then((result_plus) => {
	// 작업이 성공적으로 완료된 경우 호출되는 콜백 함수
	console.log(result_plus); // "작업 완료!" 출력
}).catch((error) => {
// 작업이 실패한 경우 호출되는 콜백 함수
console.error(error);
});