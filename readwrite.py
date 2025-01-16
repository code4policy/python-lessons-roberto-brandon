with open('name.txt', 'r') as f:
	myname = f.read()
	with open('output/hello.txt', 'w') as g:
		g.write('Hello, my name is ')
		g.write(myname)

