# whitelist-script
This repository contains a python script that creates a `.mcfunction` file that will bulk-whitelist the inputted players when placed in a datapack and run with the `/function` command. It also includes an empty data pack in case you don't already have one.

I am fully aware that one could construct this script in a matter of minutes and there are probably hundreds of others like it and it may indeed be completely useless for most people, but I built it for myself and am now sharing it with the world, because why the heck not. It's pretty simple to use but please DM me on Twitter (@Southpaw1496) or create a GitHub issue if you have any questions or concerns.

To use the script on Unix systems (macOS and Linux) open terminal and run `python3 path-to-file`, so for example if I saved the file in Downloads the command would be `python3 /Users/Southpaw1496/Downloads/whitelist-script.py`. I don't know how to use it on Windows. Simple instructions are included in the script, but if you need more detailed ones please see below.

## Sample Data Pack Usage Instructions
After creating the file using the Python script, insert it into `data/whitelist/functions`, put the datapack in the `world/datapacks` Next, in `server.properties` make sure that `function-permission-level` is set to 3 or higher to ensure that the pack is able to run whitelist commands. You can run the whitelist command using `/function whitelist:<your-file-name>`

## Detailed usage instructions (macOS, Linux)
To run the script, open your Terminal (on macOS you can press Cmd-Space and search, on Linux the location varies by distribution) and type `python3 path-to-file`, for example `python3 /Users/Southpaw1496/Downloads/whitelist-script.py`. 

The script will run and ask you for a filename. Put a name, for example `friends-whitelist` that contains no spaces, and this will be the name of the file the script creates. Then, when asked, input a list of valid Minecraft usernames seperated by spaces and nothing else. For example, adding Jeb, Notch and Dinnerbone would be `jeb_ Notch Dinnerbone`. 

The script will then convert your names into whitelist commands and write them into a file, which will be placed in the Terminal's working directory, usually your home directory (`/users/username`), and you can then put it in a data pack (see *Sample Datapack Usage Instructions* above). If the script doesn't end automatically you can now end it by pressing Ctrl-C (on both platforms).

I don't know how to run this on Windows, feel free to add instructions in a Pull Request if you would like.
