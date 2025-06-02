
with open("names.txt", "a+") as f:
    f.write("Alice\n")
    f.write("Bob\n")
    f.write("Charlie\n")
    q = f.read()
print(q)