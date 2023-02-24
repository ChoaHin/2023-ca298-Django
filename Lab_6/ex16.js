const person = {
  name: "John",
  age: 19,
  address: "DCU",
  hello: function () {
    return "Hello my name is " + this.name;
  },
};

console.log(person.hello());
