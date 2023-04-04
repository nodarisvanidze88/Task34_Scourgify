import sys
import csv
import os, glob

def main():
    user = sys.argv                                                             #   get command from user
    newList = []                                                                #   initiate empty list for new data
    if checkInput(user) == True and checkFile(user) == True:                    #   check user input and file
        with open("Task34_Scourgify/input.csv","r") as file:                        #   open exiting file with data
            info = csv.DictReader(file)                                             #   read data as dictionary
            for i in info:                                                          #   initiate for loop foe each element in exaiting dictionary
                fullName = i["name"].split(", ")                                        #   split full name by ","
                newdict = {}                                                            #   initiate blank dictionary
                newdict["First Name"] = fullName[1]                                     #   assigne first name
                newdict["Last Name"] = fullName[0]                                      #   assigne last name
                newdict["House"] = i["house"]                                           #   assigne house
                newList.append(newdict)                                                 #   append dictionary to list

        with open("Task34_Scourgify/output.csv","w",newline="") as wfile:           #   open empty csv file in write mode by line
            fildNames = ["First Name","Last Name","House"]                          #   list as header
            writeFile = csv.DictWriter (wfile, fieldnames=fildNames)                #   create header as dictionary
            writeFile.writeheader()                                                 #   write header
            for i in newList:                                                       #   initiate for loop for writing
                writeFile.writerow(i)                                                   #   write each dictionary element
    elif checkInput(user) == -1:                                                #   check if user commands are less then 3
        print("Too low commands")
    elif checkInput(user) == -2:                                                #   check if user commands are more then 3
        print("Too many commands")
    elif checkFile(user) == False:                                              #   check if file is empty or file does not exist
        print("File not found or file is empty")
        sys.exit


def checkInput(txt):                                        #   Function to check user commands length
    if len(txt) < 3:
        return -1
    elif len(txt) >3:
        return -2
    else:
        return True


def checkFile(txt):                                         #   Function to check file is empty ot not and file name
    with open("Task34_Scourgify/input.csv","r") as file:
        info = list(csv.DictReader(file))
    fileName = (glob.glob(os.path.join("Task34_Scourgify", "input.csv")))[0].split("/")
    if fileName[1] == txt[1] and  len(info) > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
