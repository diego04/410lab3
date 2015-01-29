#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
val1 = form.getvalue('name')
val2 = form.getvalue('family')
 
print "Content-Type: text/html;charset=utf-8"

print"""
<form method="post" action="index.py">
<textarea name="birthday" cols="40" rows="5">
birthday</textarea>
<textarea name="mainhobby" cols="40" rows="5">
my main hobbies
</textarea>
<br/>
<textarea name="name" cols="40" rows="5">
%s</textarea>
<br/>
<textarea name="family" cols="40" rows="5">
%s</textarea>
<br/>
<input type="submit" value="Submit">
</form>"""% (val1, val2)

print""" 
Hello my name is %s %s
""" % (val1, val2)
