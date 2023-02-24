function printer(name, callback) {
	console.log("Hello " + name);
	callback(name)
}

printer("Niv", (name) => {console.log("Hello from " + name + " call back")})


