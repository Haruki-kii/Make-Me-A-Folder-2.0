import tkinter as tk
import os
from tkinter import filedialog
import datetime
import subprocess
import shutil
from tkinter import messagebox

# Functions

def browseFolder():
    path = filedialog.askdirectory()
    if path:
        locationEntry.config(state="normal")
        locationEntry.delete(0, tk.END)
        locationEntry.insert(0, path)
        locationEntry.config(state="readonly")
        with open(fr"{localAppDataLocation}/makeMeAFolderInformationStoringFile.txt", "r") as f:
            tempFolderVar, tempExeVar = f.read().splitlines()
            tempFolderVar = "folderLocation=" + path + "\n" + tempExeVar
        with open(fr"{localAppDataLocation}/makeMeAFolderInformationStoringFile.txt", "w") as f:
            f.write(tempFolderVar)


def pythonSelected():
    extensionEntry.config(state="normal")
    extensionEntry.delete(0, tk.END)
    extensionEntry.insert(0, ".py")
    extensionEntry.config(state="disabled")

def customSelected():
    extensionEntry.config(state="normal")
    extensionEntry.delete(0, tk.END)


def createProject():
    ## VALIDATING INPUTS 
        global totalErrors
        projectNameValidation = "Pass"
        if len(projectNameEntry.get()) > 60 or not projectNameEntry.get():
             projectNameValidation = "Fail"
        for char in invalidChars:
            if char in projectNameEntry.get():
                projectNameValidation = "Fail"

        projectLocationValidation = "Pass"
        if not locationEntry.get():
             projectLocationValidation = "Fail"
        for char in invalidCharsForLocation:
            if char in locationEntry.get():
                projectLocationValidation = "Fail"

        projectExtensionValidation = "Pass"
        if not extensionEntry.get() or "." not in extensionEntry.get():
            projectExtensionValidation = "Fail"
        for char in invalidChars:
            if char in extensionEntry.get():
                projectExtensionValidation = "Fail"
    

        statusShowingLabel.config(text="")
        if projectNameValidation == "Pass":
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nProject Name is valid."
        )
        else:
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nProject Name is invalid."
        )

        if projectLocationValidation == "Pass":
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nLocation is valid."
        )
        else:
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nLocation is invalid."
        )

        if projectExtensionValidation == "Pass":
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nProject extension is valid."
        )
        else:
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nProject extension is invalid."
        )
        if projectLocationValidation == "Pass" and projectNameValidation == "Pass" and projectExtensionValidation == "Pass":
            statusShowingLabel.config(
            text=statusShowingLabel.cget("text") + "\nNow initiating."
            )


        #2026-(month)01-(day)12_1
        #(f"{year}-(month){month}-(day){day}_{n}")

            datePlusTime = str(datetime.datetime.now())
            date, time = datePlusTime.split(" ")
            year, month, day = date.split("-")
            allFolders = os.listdir(locationEntry.get())
            n = 0
            for folder in allFolders: 
                # 2026-(month)07-(day)22_1_a
                try:
                    yearForFolder, monthPlusForFolder, dayPlusForFolder = folder.split("-")
                    if yearForFolder.startswith("202"):
                        if monthPlusForFolder.startswith("(month)"):
                            monthForFolder = monthPlusForFolder.split(")")[1]
                            dayForFolder, nForFolder, projectNameForFolder = dayPlusForFolder.split("_")
                            dayForFolder = dayForFolder.split(")")[1]
                            if yearForFolder == year and monthForFolder == month and dayForFolder == day:
                                nForFolder = int(nForFolder)
                                n = max(n, nForFolder)

                except(ValueError):
                    continue


            folderPath = os.path.join(locationEntry.get(), fr"{year}-(month){month}-(day){day}_{n+1}_{projectNameEntry.get()}" )
            os.mkdir(folderPath)
            
            readmePath = os.path.join(folderPath, "Readme.md")
            with open(readmePath, "w", encoding="utf-8") as f:
                f.write(readmeText.get("1.0", tk.END).strip())

            mainFilePath = os.path.join(folderPath, f"main{extensionEntry.get()}")
            testFilePath = os.path.join(folderPath, f"test{extensionEntry.get()}")
            with open(mainFilePath, "w") as f:
                pass
            with open(testFilePath, "w") as f:
                pass

            if openVSvar.get() == 0:
                root.destroy()
                                
            else:
                #OPEN VS CODE THEN CLOSE ALL OTHER STUFF
                try:
                    codePath = shutil.which("code")
                    subprocess.Popen([codePath, folderPath])
                    root.destroy()
                except Exception as codeError:
                    totalErrors = totalErrors + str(codeError)+ "\n"
                    
                    ## THIS IS WHEN AND IF THE PROGRAM CAN'T FIND CODE.EXE THEN IT'LL CHECK THE FILE AND IF THAT DOESN'T WORK THEN IT'LL ASK THE USER ON HOLD RIGHT NOW 
                    
                    # try:
                    #     with open(fr"{localAppDataLocation}/makeMeAFolderInformationStoringFile.txt", "r") as f:
                    #                 tempFolderVar, tempExeVar = f.read().splitlines()
                    #                 locationExe = tempFolderVar.split("=")[1]
                    #                 subprocess.Popen([locationExe, folderPath])
                    # except Exception as error:
                    #     totalErrors = totalErrors + str(codeError)+ "\n"
                    #     yesNo = messagebox.askyesno("VS Code", "VS Code could not be opened, would you like to select the path to code.exe?")
                    #     if not yesNo:
                    #         codeError = "The user has decided to not choose the path to code.exe"
                    #         totalErrors = totalErrors + str(codeError)+ "\n" 
                    #     else:
                    #         while True:
                    #             try:
                    #                 pathExe = filedialog.askopenfile(
                    #                     title="Mission: Locate code.exe",
                    #                     filetypes=[("Executable files", "*.exe")]
                    #                 )
                    #                 if os.path.basename(pathExe).lower() == "code.exe":
                    #                     with open(fr"{localAppDataLocation}/makeMeAFolderInformationStoringFile.txt", "r") as f:
                    #                         tempFolderVar, tempExeVar = f.read().splitlines()
                    #                         tempExeVar = tempFolderVar + "codeExeLocation=" + codePath + "\n" 
                    #                     with open(fr"{localAppDataLocation}/makeMeAFolderInformationStoringFile.txt", "w") as f:
                    #                         f.write(tempExeVar)
                    #                     break
                    #                 else:
                    #                     locatorExeError = "The user has selected the wrong exe."
                    #                     totalErrors = totalErrors + str(codeError)+ "\n"
                    #             except Exception as error:
                    #                 totalErrors = totalErrors + str(codeError)+ "\n"
                    #                 break
def checkLog():
    mainFrame.pack_forget()
    logFrame.pack(fill="both", expand=True)
    logEntry.config(state="normal")
    logEntry.insert(1.0,totalErrors)
    logEntry.config(state="disabled")

def checkMain():
    logFrame.pack_forget()
    mainFrame.pack(fill="both", expand=True)

# Variables

localAppDataLocation = os.environ["LOCALAPPDATA"]
today = datetime.date.today()
formattedTime = today.strftime("%Y-(month)%m-(day)%d")

invalidChars = """'<>:"/\\|?*[]"""
invalidCharsForLocation = """'<>"|?*[]""" 

statusShowing = "Waiting..."

totalErrors = " "


## GUI



 
# Root properties

root = tk.Tk()

windowWidth = 800
windowHeight = 600
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
windowFromLeft = int((screenWidth-windowWidth)/2)
windowFromTop = int((screenHeight-windowHeight)/2)

root.title("Make Me A Folder")
root.configure(background="white")
root.minsize(windowWidth, windowHeight)
root.maxsize(windowWidth, windowHeight)
root.geometry(f"{windowWidth}x{windowHeight}+{windowFromLeft}+{windowFromTop}")


# MAIN FRAME

mainFrame = tk.Frame(root)
logFrame = tk.Frame(root)
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
try:
    with open(fr"{localAppDataLocation}/makeMeAFolderInformationStoringFile.txt", "r") as f:
        locationForLastFolder = (f.read().splitlines()[0]).split("=")[1]
        locationEntry.insert(0, locationForLastFolder)
        
except (FileNotFoundError):
    pass
locationEntry.config(state="readonly")

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

logButton = tk.Button(mainFrame, text="Check Log", command=checkLog)
logButton.grid(row=14, column=2)

createProject = tk.Button(mainFrame, text="Create Project", command=createProject)
createProject.grid(row=11, column=2)


# LOG FRAME

for col in range(3):
    logFrame.grid_columnconfigure(col, weight=1, uniform="cols")

for row in range(5):
    logFrame.grid_rowconfigure(row, weight=1, uniform="row")

tk.Label(logFrame, text="LOG", font=("Arial", 20)).grid(row=0, column=0)
logEntry = tk.Text(logFrame, state="disabled" )
logEntry.grid(row=2, column=0, columnspan=2, rowspan=2)
mainbutton = tk.Button(logFrame, text="Back", command=checkMain)
mainbutton.grid(row=4, column=1)

# Ender/ Last lines of code

root.mainloop()
