# Reading files in Python
#Read
f = open("fruits.txt")
content = f.read()
print(content)
f.close()
#Readline
f = open("fruits.txt")
line = f.readline()
print(line)
f.close()
#Readlines
f = open("fruits.txt", "r")
lines = f.readlines()
for l in lines:
    print(l.strip())
f.close()