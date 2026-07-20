import tkinter as tk
import os
from tkinter import filedialog



# Functions

def browseFolder():
    path = filedialog.askdirectory()
    if path:
        locationEntry.delete(0, tk.END)
        locationEntry.insert(0, path)

def pythonSelected():
    extensionEntry.config(state="normal")
    extensionEntry.delete(0, tk.END)
    extensionEntry.insert(0, ".py")
    extensionEntry.config(state="disabled")

def customSelected():
    extensionEntry.config(state="normal")
    extensionEntry.delete(0, tk.END)


# Variables

invalidChars = """'<>:"/\\|?* """


statusShowing = "Preparing..."

root = tk.Tk()

windowWidth = 800
windowHeight = 600
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
windowFromLeft = int((screenWidth-windowWidth)/2)
windowFromTop = int((screenHeight-windowHeight)/2)



## GUI



 
# Root properties

root.title("Make Me A Folder")
root.configure(background="white")
root.minsize(windowWidth, windowHeight)
root.maxsize(windowWidth, windowHeight)
root.geometry(f"{windowWidth}x{windowHeight}+{windowFromLeft}+{windowFromTop}")



# Code

mainFrame = tk.Frame(root)
mainFrame.pack(fill="both", expand=True)
for col in range(3):
    mainFrame.grid_columnconfigure(col, weight=1, uniform="cols")

for row in range(13):
    mainFrame.grid_rowconfigure(row, weight=1, uniform="row")

 #Widgets

mainLabel = tk.Label(mainFrame, text= "Make Me A Folder")
mainLabel.grid(row=0, column=0, columnspan= 3)

projectLabel = tk.Label(mainFrame, text="Project Name—")
projectLabel.grid(row=2,column=0)

projectNameEntry = tk.Entry(mainFrame)
projectNameEntry.grid(column=1,row=2)

locationLabel = tk.Label(mainFrame, text="Location—")
locationLabel.grid(column=0, row=4)

locationEntry = tk.Entry(mainFrame)
locationEntry.grid(column=1, row=4)

browseButton = tk.Button(mainFrame, text="Browse", command= browseFolder)
browseButton.grid(row=4,column=2)


extensionLabel = tk.Label(mainFrame, text="Exension— ")
extensionLabel.grid(row=6, column=0)

optionFrame = tk.Frame(mainFrame)
optionFrame.grid(row=6, column=1)

optionChoice = tk.StringVar(value="Python")

radioPython = tk.Radiobutton(
    optionFrame,
    text="Python",
    variable=optionChoice,
    value="Python",
    command=pythonSelected
)

radioCustom = tk.Radiobutton(
    optionFrame,
    text="Custom",
    variable=optionChoice,
    value="Custom",
    command=customSelected
)


radioPython.pack(side="left")
radioCustom.pack(side="left")

extensionEntry = tk.Entry(mainFrame, state="disabled")
extensionEntry.grid(column=2, row=6)
pythonSelected()

readmeLable = tk.Label(mainFrame, text="README/ Project Notes")
readmeLable.grid(row=8, column=0,)

readmeText = tk.Text(mainFrame, wrap="word")
readmeText.grid(row=8, column= 1, rowspan=1)   # I LEAVE THIS TO YOU MY FUTURE SELF. DEAL WITH IT. CIAO

clearReadme = tk.Button(mainFrame, text="Clear textbox", command= lambda: readmeText.delete("1.0", tk.END) )
clearReadme.grid(row=8, column=2)

openVSLable = tk.Label(mainFrame, text="Open VS Code")
openVSLable.grid(row=11, column=0)

openVSvar = tk.IntVar()
openVsCheckBox = tk.Checkbutton(mainFrame, variable= openVSvar, text="Check Box")
openVsCheckBox.deselect()
openVsCheckBox.grid(row=11, column=1)


statusLabelText = tk.Label(mainFrame, text="STATUS: ")
statusLabelText.grid(row=14, column=0)

statusShowingLabel = tk.Label(mainFrame, text=statusShowing)
statusShowingLabel.grid(row=14, column=1)

createProject = tk.Button(mainFrame, text="Create Project")
createProject.grid(row=11, column=2)


## VALIDATING INPUTS 

# projectNameValidation = "Pass"
# if len(projectNameEntry) > 60 or not projectNameEntry:
#      projectNameValidation = "Fail"
# for char in invalidChars:
#     if char in projectNameEntry:
#         projectNameValidation = "Fail"

# projectLocationValidation = "Pass"
# if not locationEntry:
#      projectLocationValidation = "Fail"
# for char in invalidChars:
#     if char in locationEntry:
#         projectLocationValidation = "Fail"

# projectExtensionValidation = "Pass"
# if not extensionEntry:
#     projectExtensionValidation = "Fail"
# for char in invalidChars:
#     if char in extensionEntry:
#         projectExtensionValidation = "Fail"


# Ender/ Last lines of code

root.mainloop()
