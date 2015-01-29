#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgi
#import cgitb
#cgitb.enable()

form = cgi.FieldStorage()


val1 = form.getvalue('name')
val2 = form.getvalue('family')
val1 = form.getvalue('birthday')
val2 = form.getvalue('mainhobby')

print "Content-Type: text/html;charset=utf-8"

print"""
<form method="post" action="page2.py">
<textarea name="name" cols="40" rows="5">
Enter firstname here...
</textarea>

<textarea name="family" cols="40" rows="5">
Enter lastname here...
</textarea>

<br/>
<input type="submit" value="Submit">
</form>"""


print""" 
Hello my name is %s and my last name is %s
""" % (val1, val2)
print "<br/>"
print""" 
Hello my birthday is %s and my hobby is %s
""" % (val1, val2)
