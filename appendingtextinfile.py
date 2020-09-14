with open("files/fruits.txt", "a+") as myfiles: # + is added to read and write both
    myfiles.write("\nokra")
    myfiles.seek(0) #to take the cursor at 0 position
    content = myfiles.read()

print(content)