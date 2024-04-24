f = open("test.txt", "r")

# to read the content of test.txt as a string
f.read()

# to read the content of test.txt as a list where each element of the list is a row in the file
f.readlines()

# to bring back the cursor at the very beginning of test.txt before reading from the file once again
f.seek(0)

# to get the current position of the cursor inside test.txt
f.tell()

# to get the current mode in which test.txt is open
f.mode

# to open a file for appending and reading at the same time.
f = open("test.txt", 'a+')

# to write in a file opened for write
f = open("test.txt", "w")
f.write('python')
f.close()

# to write a list of strings
f = open("test.txt", "w")
f.writelines(['python', ' ', 'and', ' ', 'java'])
f.close()

# to write the string python and also close test.txt properly using the with statement.
with open('test.txt', 'w') as f:
    f.write('python')
    
# to delete the entire content of a file
open('test.txt', 'w').close()

f = open("test.txt", "r+")
f.truncate()


