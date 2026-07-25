# Notes

12th of july 2026— what did i do today? uh...
let's see...

1. Officially started this project
2. Made the frame on which I'll make the application in Tkinter. There'll be another frame for... for... log
3. Wrote 60-70 lines of code... 
4. Debugged everything... and I mean everything...
What else did I do again... uh...
uh... i'll just upload a picture?
5.Picture of what I made for now... 
 https://media.discordapp.net/attachments/1067768004743532614/1525789409742426132/FAF811FB-8AA5-4CE4-ACD0-2C065F5E6844.png?ex=6a54a99f&is=6a53581f&hm=14af1788b8c5519d0af615430283bad6e454e0610117a219c8f5c0610f5c40b0&=&format=webp&quality=lossless&width=935&height=737


19th of july 2026—
    I didn't do anything in b/w

    i forgot what i did on 19th probably made the validation stuff. half of it? mostly... like 90% (this is me from 22/07/2026)

(I made an AI write this 'cause I have a fever and i am too tired, that's why it's so bright... Don't worry though, the code is mine(that's why it's so bad). I don't vibe code)

# 2026-07-22

## Progress Today

### ✅ Input validation (Partially complete)

* Added validation for:

  * Project name
  * Project location
  * Project extension
* Improved status messages to report validation results.
* Discovered and fixed the bug where spaces were accidentally treated as invalid characters.

### ✅ Automatic project folder creation

* Project folders are created in the selected location.
* Folder names follow the format:

  ```
  YYYY-(month)MM-(day)DD_N_ProjectName
  ```
* The program correctly detects existing folders created on the same day and increments `N` automatically.

### ✅ Project file creation

* Implemented creation of the initial project files inside the new folder.
* README contents are taken from the Notes/README text box.

### ✅ Remember last used location

* Program now stores the last selected project location in AppData.
* On startup, the saved location is loaded automatically into the location entry.

### ✅ Planned VS Code integration

* Decided on the following workflow:

  1. Try launching VS Code using the `code` command.
  2. If that fails, try a previously saved `Code.exe` path.
  3. If that also fails, ask the user to locate `Code.exe`.
  4. Save the chosen path for future launches.

---

# 2026-07-23

## TODO

* Implement the VS Code launch workflow.
* Save and load the `Code.exe` location from AppData.
* Open the newly created project folder in VS Code.
* Close the application automatically after a successful project creation.
* Create the Error/Logs frame.
* Move status/error reporting into the Error/Logs frame.
* Build the first `.exe` using PyInstaller.
* Test the executable on a different computer.
* Fix any issues found during testing.
