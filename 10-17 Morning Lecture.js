//---cats---

var images = document.getElementsByTagName("img");
for (var i = 0; i < images.length; i++) {
	
}

// . => class
// # => id

<script></script>

// or

<script src = "app.js"></script>

// DOM = html document tree = document object model 

// the document object lets us access the html of the website

// oh hey - the document object is a dictionary!
// e.g.

document.body // => body tag 

document.body.classlist // => list of classes on the body tag 

// gotta search for the element 
// e.g., by id
// html
<img id="mainpicture" src="http://placekitten.com/200/300">
// javascript 
var img = document.getElementById('mainpicture');
// now change it
img.src = "newimgurl.png"; 

// or by tag name
document.getElementsByTagName(tagName);
var images = document.getElementsByTagName(img);
// returns a list of images (array)
// you can access ind. images by index 

// or by class name 
document.getElementsByClassName(className);

// back to var img
img.setAttribute('src', 'http://placekitten.com/100/500');
img.className = "picture";

//
var sponsers = document.getElementsByClassName("img-circle"); 
// can't do
sponsers.src = "whatever";
// because sponsers is an arraylist
// so do this
sponsers[0].src = "catpicture.png"; 
// or
sponsers[0].setAttribute("src","catpicture.png"); 

// innerHTML helps you change the content within the tags 
var pageNode = document.getElementsByTagName('body')[0];
pageNode.innerHTML += "...just adding this bit at the end of the page.";