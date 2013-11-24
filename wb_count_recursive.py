import string 

def count_recursive(l, i): 
	if len(l) == 0:
		return 0
	else: 
		element = l[-1]
		if element == i: 
			return 1 + count_recursive(l[:-1], i)
		else: 
			return count_recursive(l[:-1], i)

def test_count_recursive():
	test_list = [8,9,0,6,8,6,8,3,3,3,3,5,4]
	result = count_recursive(test_list,8)
	if result == 3: 
		return "count_recursive: passed"
	else:
		return "count_recursive: failed"

print test_count_recursive

# how do we tell if a function runs in O(log(n))
# input splits roughly in half every time 
# e.g. 8 splits in half 3 times

# takes a sorted list
def in_list(l, i):
	if len(l) == 0:
		return False
	middle_index = len(l)/2
	if l[middle_index] == i: 
		return True 
	elif l[middle_index] > i: 
		return in_list(l[:middle_index], i)
	else: 
		return in_list(l[middle_index + 1:], i)

def test_in_list(): 
	list_zero = []
	i = 3
	print "Should return false: " + str(in_list(list_zero, i))
	list_one_t = [3]
	print "Should return true: " + str(in_list(list_one_t, i))
	list_one_f = [2]
	print "Should return false: " + str(in_list(list_one_f, i))
test_in_list()
	# etc. 

# could do this with a while loop 
# it's better to do the while loop way 
# store start and end indices 

def flip_words(string):
	# split list on spaces
	# reverse each word
	# reconcatenate and return 
	words = string.split()
	storage = []
	for word in words: 
		storage.append(str(reversed(word)))
	new_string = ""
	new_string = " ".join(storage)
	return new_string

print flip_words("I love you")

# write out steps
# e.g. input and output

# reverse a list
# return a copy 
# e.g. input: l = [0,1,2,3,4]
# e.g. output: l = [4,3,2,1,0]
# create empty list
# iterate through list backwards
# append each item to the new list

def reverse_copy(l): 
	flipped = []
	while len(l) != 0:
		last_item = l.pop()
		flipped.append(last_item)
	return flipped

print reverse_copy([0,1,2,3,4])

# this is O(n)
# space complexity: twice the list (2n) [linear]
# or you could do a reverse for loop

# lambda 

# js: 

# function foo(x) {
# 	console.log(x);
# }

# var foo = function(x) {
# 	console.log(x);
# }

# Works for both: 
# bar = foo;
# bar(5); => 5

# A lambda is a function with no name
# e.g. var foo (foo is a reference, not a name)

# python 
# foo = lambda x: x + 1

# uh...let's say you want to sort on the second element of the tuples in a list
# DSU = decorate sort undecorate 

# sorted(l, key = second)

# def second(x):
# 	return x[1]

# or sorted(l, key = lambda x: x[1])

# this is called a first class function
# it is when a function is passed to another function 

def reverse_in_place(l): 
	start = 0
	end = len(l) - 1
	while (start < end): 
		temp = l[start]
		l[start] = l[end]
		l[end] = temp
		start += 1
		end -= 1 
	return l 

print reverse_in_place([0,1,2,3])