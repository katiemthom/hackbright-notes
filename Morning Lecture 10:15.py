"""
For major concept interests:
	- wikipedia it
	- look at the uses 
	- maybe you'll find an application to implement 
	- what if I do this on twitter? or on pictures of cats? etc.

e.g. Structure from motion: 
	- given photos of a think, can you reconstruct the original thing? 
	- check out the struction from motion pipeline on youtube
	- or: "iphone video to point cloud with visual sfm"
	- actually pretty cool 

first Liz talks about projects
	- three categories traditionally: webapps, webapps + ______, crazy shit
	- they all have a spectrum of difficult within them
	- and you can do something great with all of them

webapps: 
	- architecture 
	- web technologies 
	- relevant

webapps + ______ :
	- most offers come from here...
	- also relevant
	- natural language processing 
	- computer vision
	- optical character recognition 
	- signal processing 
	- machine learning
	- data viz
	- data analysis 
	- algorithms 

crazy shit: 
	- operating systems
	- compilers
	- security/hacks
	- database engines  
	- less jobs here but they pay a shit ton 

now Christian shows us what Flask is doing: 
	- sockets are a way to exchange info
	- you open them...
	- a web browser...
"""

@app.route("/test")
def test():
	return "This is a test"

"""
url "localhost:5000/test":
	- what does it dooooooo? 
	- christian sets up a thing in his terminal to look at what's happening on port 5000
	- the browser opens a socket and sends strings over
	- you also see: "GET /test" which is the browser asking the server for /test 
	- so flask sets up a loop that reads from the socket 
	- and prints the return value back to the browser 
	
faq: 
	- so the socket is between the browser and the server
	- and the browser opens the socket for each url 
	- type in url, browser prints results 
	- app.route creates a dictionary that says if you get the string "/test" call the function test()
	- django is like flask, but different syntax 
	- getting django set up is kind of a bitch though 

what's a decotrator do: 
	- a decotrator is a function that takes in a function and returns a new function 
	- so it wraps the function underneath it in another function
	- (the one that makes it work in crazy flask land?)
	- basically connects the url and the function to execute

jinja is a templating language 

app = Flask(__name__)
	- app is an object
	- and it has a menthod calls route
	- and it comes from Flask 

instead of returning a success page we could have returned a redirect
to a display project page that takes a project title arg 

never call routed functions 
"""


