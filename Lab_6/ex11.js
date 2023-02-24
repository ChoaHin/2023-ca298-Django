function add(x, y) {
	return x + y;
}

function printer(callback, num1, num2) {
	console.log(add(num1,num2));
}

printer(add,6,9);
