#!/usr/bin/python

import time

print 'Content-Type: text/html'
print
print '<html>'
print '<head><title>Hello from Python</title></head>'
print '<body>'
print '<h2>Time is:' + time.ctime() + '</h2>'
print '</body></html>'
