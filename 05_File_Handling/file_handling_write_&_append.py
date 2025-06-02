# Writing in python
# write()
f = open("fruits.txt", "w")  # Open file in write mode
f.write("Apple\n")
f.write("Banana\n")
f.write("Cherry\n")
f.close()  # Close the file
# Append to a file
f = open("fruits.txt", "a")  # Open file in append mode
f.write("Date\n")
f.write("Yolk\n")
f.write("Elderberry\n")
f.close()  # Close the file

with open("fruits.txt", "r") as f:  # Using 'with' to handle file closing automatically
    print(f.read())
