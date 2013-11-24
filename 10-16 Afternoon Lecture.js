/*
Kelsey's Tech Talk: RSS
-------------------------------------------------

---RSS---
- RSS = Really Simple Sindication
- Glorified XML file
- text, audio, video

---XML---
- eXtensible Markup Language
- used to organize content 

---RSS Reader---
- displays XML in a friendly way 
- feedly.com

---follow-up---
- tor.com is a cool tech site 

---API---
- feedly has an API

More JavaScript
-------------------------------------------------
*/

// objects are dictionaries

// e.g.

var aboutMe = {
	hometown: "Dallas, TX",
	hair: "brown"
};

// you can next objects in objects

// propertyName: propertyValue,

// dot notation 
var myHair = aboutMe.hair; 
// bracket
var myHair = aboutMe["hair"]; 

// e.g. change things
aboutMe.hair = "blond";

// e.g. add things
aboutMe.gender = "female"; 

// delete things
delete aboutMe.gender; 

// arrays of objects 
var myCats = [
  {name: "Meeko", 
  age: 2},
  {name: "Jean Clawes",
  age: 12}
];

var meeko = myCats[0];

for (var i = 0; i < myCats.length; i++) {
  var myCat = myCats[i];
  console.log(myCat.name + ' is ' + myCat.age + ' years old.');
}

// using var inside an object definition will make the variable private

// functions in objects are called methods
// syntax

var meekoTheCat = {
  age: 2,
  furColor: 'Black',
  meow: function() {
    console.log('meowww');
  },
  eat: function(food) {
    console.log('Pfft, I hate ' + food);  
  },
  sleep: function(numMinutes) {
    for (var i = 0; i < numMinutes; i++) {
      console.log('z');
    }
  }
};
meekoTheCat.meow();
meekoTheCat.eat('brown mushy stuff');
meekoTheCat.sleep(10);

// you can have unnamed functions
// () => run the code inside this var 
// e.g.
(function() {console.log("instant function!")})()
// => instant function! 
// or 
(Function("return 5"))()
// => 5 
// functions that have no name are anonymous 

// python: self
// js: this 

// the master object is window (the global context)

// classes are kinda like objects, but are set = to a function
// e.g.
var Cat = function(name,furColor){
	this.name = name; 
	this.furColor = furColor; 
}
var tribbles = new Cat("Tribbles", "black");
var jean_claws = new Cat("Jean Claws van Kitty", "tuxedo");
var kunta_kittay = new Cat("Kunta Kittay", "striped"); //My parents named this one.
// well, I suppose classes help you make objects with similar properties 

typeof tribbles; 
// => 'object' 


// + 1
