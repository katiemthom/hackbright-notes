# Generators
# ----------

def f(x):
	return x * 2

# if you give 2, you should always get 4!

# Generators let you break this rule

def f(x): 
	yield x*2
	yield x*3
	yield x*4

# f(2) return 4 then 6 then 8 

# A Generator: 
# Captures the state of a function
# And then next time returns the next yield 
# You have to use loops!

something = xrange(1000)

# xrange is a generator 

# you can do
for x in something: 
	return x

# printsthe numbers 1-999

# takes less memory than range

# Can you print the first number in something? 

x = something.__iter__()
x.next() # 0
x.next() # 1
# etc 

f = open('superbigfile')
x = f.__iter__()
x.next() # returns one line
x.next() # returns the next line

# A generator is an object that is like a list that can produce one element at a time,
# Takes up less space
# Use it? Loop through it
# Create it? Use yield 

# List comprehension
# ------------------

x = range(10)

# we want to run every element in x through the function double

def double(y):
	return 2*y

new_list = []

for item in x: 
	new_list.append(double(item))]

# This is list comprehension 
# Put a for loop inside a list declaration

my_extra_new_list = [ double(item) for item in x ]

odds = [ item for item in numbers if odd(item) ]

a = range(10)
b = range(10,20)
my_tuples = zip(a,b) # [(0,10),(1,11)...etc...]

for t in my_tuples: 
	print t[0], t[1]

for t_1, t_2 in my_tuples: 
	print t_1, t_2 # unpacking a tuple 

t_1, t_2 = my_tuples[0] # another unpack 

reversed_tuples = [ (b,a) for a, b in my_tuples ]

# stupid python tricks 
import string
a = list(string.ascii_lowercase)
b = range(26)
c = zip(a, b)
d = dict(c)

# pretty cool

# peter norvig has a sudoku solver!!
# norvig.com/sudoku

reversed_tuples = ( (b,a) for a, b in my_tuples )

# makes a generator! 

# I should maybe look up decorators 

def app_route(fn, route):
	global ROUTES
		def routed_fn(*args, **kwargs):
			ROUTES[route] = fn
			fn(*args, **kwargs)
		return routed_fn

# -ish
# basically takes your route and puts in in a dictionary 

# args and kwargs
# ---------------

# what if you want to make a function
# that can have an unlimited # of args

def sum(a, b, c=0, d=0, e=0):
	return a+b+c+d+e

# not extensible :(

def sum(*args): 
	total = 0
	for x in args: 
		total += x
	return total

# the * stores the arguments in a tuple (you could call it *cats)

# def ages(liz=25, david=25, etc....)

# You don't ever really use these...

# **kwargs is like the dictionary equivalent for *args

def ages(**kwargs):
	print kwargs

ages(liz=25) # {'liz': 25}

def config(host = None, port = None, tod = None, atmospheric_presure = None):
	pass

args = {'host': 'localhost', 'port': 5000}

config(**args) # splits up a dict and passes it to a function
