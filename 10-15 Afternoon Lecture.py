# GET and POST
# ____________

# listen to the port
# $ sudo ngrp -W byline -q -d lo0 "" tcp port 5000

# 127.0.0.1 => local host 
# GET / => get me the page at / 
# GET tells you whatever url you're getting is informational

# with a form
# GET /process?hamster=test HTTP/1.1.

# big flaw => you can see the args
# security!!!!

# POST
# e.g. <form method = "POST">

# GET is only for getting

# Network tab on dev tools inspector 
# POST separates the args from the rest of the url 

# use request.args.get for GET methods
# use request.form.get for POST methods

# should return a redirect after a POST
# that's good because then the process step
# isn't recorded in the browser history 

# you can send things through the url w/o the ? too...

# javascript can access things after the ?

# input type = "submit" value = "GO" name = "send me back"
# GO is what you want the button to say 

# use jquery and bootstrap to help out with 
# different browsers 

# network tag can be super helpfup 
# other input types: 
# textarea 
# chrome only: 
# date 
# number 