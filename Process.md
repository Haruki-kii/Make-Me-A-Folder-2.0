# Notes

Okay, 26th of July, the same year, I'm kinda mostly done with this one. It took me so long because of the exams, ugh. And now I have more. Ugh, again.

12th of july 2026— what did i do today? uh...
let's see...

1. Officially started this project
2. Made the frame on which I'll make the application in Tkinter. There'll be another frame for... for... log
3. Wrote 60-70 lines of code... 
4. Debugged everything... and I mean everything...
What else did I do again... uh...
uh... i'll just upload a picture?

19th of july 2026—
    I didn't do anything in b/w (exams, yay)

    i forgot what i did on 19th probably made the validation stuff. half of it? mostly... like 90% (this is me from 22/07/2026)


2026-07-22

Input validation

Added validation for:

  * Project name
  * Project location
  * Project extension
* Improved status messages to report validation results.
* Discovered and fixed the bug where spaces were accidentally treated as invalid characters.

Automatic project folder creation

* Project folders are created in the selected location.
* Folder names follow the format:

  ```
  YYYY-(month)MM-(day)DD_N_ProjectName
  ```
* The program correctly detects existing folders created on the same day and increments `N` automatically.

Project file creation

* Implemented creation of the initial project files inside the new folder.
* README contents are taken from the Notes/README text box.

Remember last used location

* Program now stores the last selected project location in AppData.
* On startup, the saved location is loaded automatically into the location entry.

Plans for VS opening

  1. Try launching VS Code using the `code` command.
  2. If that fails, try a previously saved `Code.exe` path.
  3. If that also fails, ask the user to locate `Code.exe`.
  4. Save the chosen path for future launches.

---

To do for 2026-07-23

* Implement the VS Code launch workflow. (okay)
* Save and load the `Code.exe` location from AppData. (kinda? but i commented out the code. it's hell because i made a mess.) (i completed it on 26th, or today)
* Open the newly created project folder in VS Code. (was kinda...too easy. as long as shutil can find code.cmd i guess)
* Close the application automatically after a successful project creation. ( One line... or two cause two cases )
* Create the Error/Logs frame. (base done)
* Move status/error reporting into the Error/Logs frame. (eh sure. did that)
* Build the first `.exe` using PyInstaller. (didn't do that)
* Test the executable on a different computer. (i'll do that today actually. It's 25th today)
* Fix any issues found during testing. (i didn't test so... yk) 
