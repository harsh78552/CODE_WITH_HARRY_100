"""with open("Myfile.txt", "r") as f:
    print(type(f))
    #  move to the 10 bytes in the file
    f.seek(10)

    # Read the next 5 bytesl̥
    print(f.tell())
    data = f.read(5)
    print(data)"""

with open("Myfile.txt", "w") as f:
    f.write("Namaste , How are you ?")
    f.truncate(5)
with open("Myfile.txt", "r") as f:
    print(f.read())
