const getTime = () => {
	let today = new Date();
	let hours = today.getHours();
	console.log(hours);
	let minutes = today.getMinutes();
	console.log(minutes);
	let seconds = today.getSeconds();
	console.log(seconds);
	let milliseconds = today.getMilliseconds();
	console.log(milliseconds);
	return (
	  String(hours) + String(minutes) + String(seconds) + String(milliseconds)
	);
  };

console.log(getTime());