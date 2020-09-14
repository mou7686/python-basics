import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st1"]) #to calculate the mean of 1st column
    else:
        print("File doesn't exist")
    time.sleep(10)