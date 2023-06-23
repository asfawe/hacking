function sum(a, b) {
	return a + b;
}

function asyncTask() {
	return new Promise((resolve, reject) => {
	  // 비동기 작업 수행
	  setTimeout(() => {
		const randomNumber = Math.random();
		if (randomNumber < 0.5) {
		  resolve(sum(1,1)); // 작업이 성공적으로 완료된 경우
		} else {
		  reject("작업 실패!"); // 작업이 실패한 경우
		}
	  }, 1000);
	});
  }
  
  function main() {
	asyncTask()
	  .then((result) => {
		// 첫 번째 then()의 콜백 함수 (성공적인 경우)
		console.log(result); // 작업 결과 출력
		return result; // 다음 then()으로 결과 전달
	  })
	  .then((result) => {
		// 두 번째 then()의 콜백 함수 (성공적인 경우)
		console.log(result); //
		console.log("두 번째 then() 실행됨");
		// 추가적인 작업 수행
		return result; // 다음 then()으로 결과 전달
	  })
	  .catch((error) => {
		// 에러 처리를 위한 catch() 콜백 함수
		console.error(error); // 에러 메시지 출력
	  });
  }
  
  main(); // main 함수 실행