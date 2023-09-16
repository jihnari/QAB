import sys
import re


for line in sys.stdin:
	print ("line: ", line)
	
	# find time
	r_bracket_idx = line.find("]")
	time = line[1:r_bracket_idx-3]
	
	
	# find name
	colon_idx = line.find(":", line.find(":")+1)
	name = line[r_bracket_idx+2:colon_idx]
	
	
	# grab message content 
	msg = line[colon_idx+2:]
	
	
	# name switch 
	if name == "Lar | anti-soup squadron":
		print ("<p><span class=dc-name color-purple>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")
	if name == "Reeves | Soup Switzerland":
		print ("<p><span class=dc-name color-green>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")
	if name == "crawler | anti-soup captain":
		print ("<p><span class=dc-name color-blue>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")
	if name == "Volanna | Soup is good":
		print ("<p><span class=dc-name color-red>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")
	if name == "Shuttai | soup radical 🤍":
		print ("<p><span class=dc-name color-forest>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")
	if name == "Squish! | favorite child":
		print ("<p><span class=dc-name color-green>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")
	

    
	
	
		'''
	print ("time:", time)
	print ("name:", name)
	print ("msg:", msg)
	print ("-----")
	'''
	
	# print ("<p class=shift-up><span class=dc-name color-default>", name, "</span> <span class=dc-time-stamp>Today at", time, "</span><br />", msg, "</p>")