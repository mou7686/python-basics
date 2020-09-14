import time
while True:
    with open("files/fruits.txt") as myfiles:
        print(myfiles.read())
        time.sleep(10)