import time
import os

while True:
    if os.path.exists("files/fruits.txt"):
        with open("files/fruits.txt") as myfiles:
            print(myfiles.read())
    else:
        print("File doesn't exist")
    time.sleep(10)