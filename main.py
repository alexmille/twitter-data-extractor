import sys
import os
from credentials import *
from extractTweets import get_all_tweets
from followersList import get_all_followers

file_dir = os.path.join(os.path.dirname(__file__))

print("Hello")
print("Welcome to the python Twitter data extractor !")

# Erase twHandle file
f = open("twHandle.txt", 'r+')
f.truncate()
f.write(raw_input("Please enter your Twitter handle: @"))
f.close()

m = open("twHandle.txt", 'r')
newHandle = (m.read())
print newHandle
m.close()
# Check if the credentials file is filled properly
credCheck = []
if (consumer_key == ""):
    credCheck.append("Consumer Key")
elif (consumer_secret == ""):
    credCheck.append("Consumer Secret")
elif (access_key == ""):
    credCheck.append("Access Key")
elif (access_secret == ""):
    credCheck.append("Access Secret")
# Returns missing credentials
if len(credCheck) > 0:
    print("Please insert the following fields in the credentials file and start again !")
    for p in credCheck:
        print ("\t - " + p)
    sys.exit()
else: 
    print("Your credentials file looks perfect :D")

while True:
    menu = int(input("\nWhat do you want to do ?\n"
     "1 Extract Tweets\n"
     "2 List my Followers\n"
     "3 Change Twitter handle\n"
     "4 Exit\n"))

    m = open("twHandle.txt", 'r')
    newHandle = (m.read())
    m.close()

    if menu < 5:
        if (menu == 1):
            print("OK, I'll extract " + newHandle +  " tweets")
            get_all_tweets(newHandle)
        elif (menu == 2):
            print("OK, I'll extract " + newHandle + " followers")
            get_all_followers(newHandle)
        elif (menu == 3):
            f = open("twHandle.txt", 'r+')
            f.truncate()
            f.write(raw_input("Please enter your Twitter handle: @"))
            f.close()
        elif (menu == 4):
            sys.exit()
    else:
        print("Wrong number, try again buddy !\n")
            
