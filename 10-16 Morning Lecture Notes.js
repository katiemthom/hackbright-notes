/*undefined: not defined yet
null: explicitly empty

reserved words: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Reserved_Words?redirectlocale=en-US&redirectslug=JavaScript%2FReference%2FReserved_Words

why would you want to start something with a dollar sign? 
jquery aliases itself to the $
$ is the alias of jquery

$variableName => "hey contained within this variable is a jquery element"

typeof variableName
console.log(typeof y);
*/

// commments 
//
/*multi-line*/

// function syntax
function sayMyName() {
	console.log('Hi Liz!'); 
}

sayMyName();

// functions are objects!

// this is how you wanna go it 
var sum = function(a,b) {
	return a + b; 
}; 

// think of functions as variables! 
// that have valid js strings inside

// () is the invocation operator
// it runs the code inside the variable

// control statements (for, if, etc.) don't have ; 

// in js you can't name args in the input 
// e.g. sum(x = 5, y = 10)
// can't do it 

// you can do this:

/*var declares a variable and also sets the context
depending on where the variable is declared */

// yay: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide?redirectlocale=en-US&redirectslug=JavaScript%2FGuide

// if statement syntax

var x = 5; 

if (x > 0) {
	console.log('x is a positive number!'); 
} else {
	//Do something else. 
}

// === strict equality 
// compares type
// unlike python which doesn't allow you to compare different types at allow

// && => and
// || => or 
// truth-y: anything not false-y
// e.g. "cat" is true
// false-y: false, "", 0, undefined, none
// empty lists are true 

// arrays: lists
// objects: dictionaries

// if you do an assignment: that's true!
// e.g. if (cats = 5) will be true no matter what 
// it will not check to see if cats is actually five 

/*
(false && anything) => false 
(true || anything) => true
/*

/*JS evaluates logical operators from left to right and stops evaluating as soon as it knows the answer.*/

// else if instead of elif 

// switch statements 
// instead of 7 else if statements
var numCats = 5; 

switch numCats
	case 1: 
	case 2: 
		// case 1 falls through
		console.log("1 or 2 cats");
		break;
	case 5: 
		//do something
		break; 
	default: 
		//do something
		break;
	}

// while loop syntax

var x = 0; 
while (x < 5) {
	console.log(x); 
	x = x + 1; 
}

// for loop syntax
/*
for (initialize; condition; update) {
	// statements to repeat
}
three statements up there!
initialize scopes the variable to the loop
*/


for (var i = 0; i < 5; i = i + 1) {
	console.log(i); 
}

for (var current = 100; current < 200; current++) {
	console.log('Testing' + current); 
	if (current % 7 == 0) {
		console.log('Found it! ' + current); 
		break; 
	}
}

// break ends things
// continue only ends that iteration 

// arrays = list
// datatype
// no slicing
// ordered

// length syntax
var rainboxColors = ['red', 'orange']; 
// rainboxColors.length returns 2

// adding things to an array 
rainboxColors[2] = 'yellow';

rainboxColors.push('green'); 





//+3