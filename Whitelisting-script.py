print("Welcome to Southpaw#1496's \"Whitening\" script. This script will take a list of Minecraft usernames and turn them into a .mcfunction file to whitelist them in bulk. Note that for this script to work, function-permission-level must equal 3 or higher in server.properties. If you do not already have a datapack in which to put the outputted mcfunction, one I made earlier is available on the GitHub repository (or included if you downloaded a release release.) \n")

fileName = input("Please input the name if the file you wish to write to. It should contain no spaces, and no file extension: ")
nameInput = input("Please input a list of names to input, seperated by commas and spaces eg. jeb_ Notch Ulraf : ")
nameList = nameInput.split()
for i in nameList:
    f = open(fileName + ".mcfunction", "a" )
    f.write("\n whitelist add " + i)

print("Your file is now saved in the working directory of the terminal, usually the home folder (/users/username). Take it and put it in your datapack, or if you don't have a datapack you can use the example one included in the repository.")