#Files Tutorial Assignment 

#Opening files 
f = open("test.txt", "r")
f = open("test.txt", "w")
f = open("test.txt", "a")
f = open("test.txt", "r+")

#Print name of file
print(f.name)
print(f.mode)

#Close file
f.close()

#Reading Files
with open("test.txt", "r") as f:
	pass

	#Small Files
	f_contents = f.read()
	print(f_contents)

	#Big Files
	f_contents = f.readlines()
	print(f_contents)

    #With the extra lines
	f_contents = f.readline()
	print(f_contents)
	f_contents = f.readline()
	print(f_contents)

	#Without the extra lines
	f_contents = f.readline()
	print(f_contents, end = '')
	f_contents = f.readline()
	print(f_contents, end = '')

	#Iterating through the file
	for line in f:
		print(line, end = '')

	#Printing by characters
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')

	#Iterating small
	size_to_read = 100
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size_to_read)

	#Iterating with 10 characters
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	f.seek(0)
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	print(f.tell())
	while len(f_contents) > 0:
		print(f_contents, end = '*')
		f_contents = f.read(size_to_read)
print(f.mode)
print(f.closed)
print(f.read())


##Writing Files!

#The Error
with open("test.txt", "r") as f:
	f.write("Test")

#Writing Starts
with open("test2.txt", "w") as f:
	pass
	f.write("Test")
	f.seek(0)
	f.write("Test")
	f.seek("R")

#Copying Files
with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)

##Copying image!

#The Error
with open("shelby.jpg", "r") as rf:
	with open("shelby_copy.jpg", "w") as wf:
		for line in rf:
			wf.write(line)

#Copying the image starts, without chunks
with open("shelby.jpg", "rb") as rf:
	with open("shelby_copy.jpg", "wb") as wf:
		for line in rf:
			wf.write(line)

#Copying the image with chunks
with open("shelby.jpg", "rb") as rf:
	with open("shelby_copy.jpg", "wb") as wf:
		chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

##THE END
