# We know the first 5 characters will be NCTG{
# Judging by the characters this iss ASCII+44, then -50, then +44 etc
# Which yields something close enough to the flag that you can fill in the gaps
string="\"u(yOGB=F?@93G9;3FIB8HQ"
i = 0
for char in string:
	if i%1 == 0:
		print chr(ord(char)+44),
	else:
		print chr(ord(char)-50),
	i = i + 1
