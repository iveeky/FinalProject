import csv
import tkinter as tk
from tkinter import messagebox

class newHireProgram:
    def __init__(self, dataEntry):
        self.dataEntry = dataEntry
        dataEntry.title("New Hire Onboarding Form")

        # Creating widgets that label the user's input.
        self.companyLabel = tk.Label(dataEntry, text="Company Name:")
        self.companyLabel.grid(row=0, column=0)
        self.companyInput = tk.Entry(dataEntry)
        self.companyInput.grid(row=0, column=1)

        self.managerNameLabel = tk.Label(dataEntry, text="Manager Name:")
        self.managerNameLabel.grid(row=1, column=0)
        self.managerNameInput = tk.Entry(dataEntry)
        self.managerNameInput.grid(row=1, column=1)

        self.managerEmailLabel = tk.Label(dataEntry, text="Manager E-mail:")
        self.managerEmailLabel.grid(row=2, column=0)
        self.managerEmailInput = tk.Entry(dataEntry)
        self.managerEmailInput.grid(row=2, column=1)

        self.newHireNameLabel = tk.Label(dataEntry, text="New Hire's Name:")
        self.newHireNameLabel.grid(row=3, column=0)
        self.newHireNameInput = tk.Entry(dataEntry)
        self.newHireNameInput.grid(row=3, column=1)

        self.userStartLabel = tk.Label(dataEntry, text="New Hire Start Date:")
        self.userStartLabel.grid(row=4, column=0)
        self.userStartInput = tk.Entry(dataEntry)
        self.userStartInput.grid(row=4, column=1)

        self.jobTitleLabel = tk.Label(dataEntry, text="Job Title:")
        self.jobTitleLabel.grid(row=6, column=0)
        self.jobTitleInput = tk.Entry(dataEntry)
        self.jobTitleInput.grid(row=6, column=1)

        self.newHireEmailLabel = tk.Label(dataEntry, text="Desired New Hire E-mail:")
        self.newHireEmailLabel.grid(row=7, column=0)
        self.newHireEmailInput = tk.Entry(dataEntry)
        self.newHireEmailInput.grid(row=7, column=1)

        self.emailListLabel = tk.Label(dataEntry, text="Desired E-mail Lists:")
        self.emailListLabel.grid(row=5, column=0)
        self.emailListInput = tk.Entry(dataEntry)
        self.emailListInput.grid(row=5, column=1)

        self.computerSelectLabel = tk.Label(dataEntry, text="Does the user need a computer:")
        self.computerSelectLabel.grid(row=8, column=0)
        self.computerInput = tk.Entry(dataEntry)
        self.computerInput.grid(row=8, column=1)

        # Button to export data.
        self.exportButton = tk.Button(dataEntry, text="Submit", command=self.exportData)
        self.exportButton.grid(row=9, column=6)

        exitButton = tk.Button(self.dataEntry, text="Exit", command=self.userExit)
        exitButton.grid(row=9, column=0)

        # Function will be called to exit the program once the exit button is clicked.
    def userExit(self):
        exit()

        #This funcation submits the data from the user.
    def exportData(self):

        companyName = self.companyInput.get()
        managerName = self.managerNameInput.get()
        managerEmail = self.managerEmailInput.get()
        newHireName = self.newHireNameInput.get()
        startDate = self.userStartInput.get()
        jobTitle = self.jobTitleInput.get()
        newHireEmail = self.newHireEmailInput.get()
        emailLists = self.emailListInput.get()
        computerSelect = self.computerInput.get()

        # This creates the confirmation window for the user to review.
        confirmation_message = f"Company Name: {companyName}\nManager Name: {managerName}\nManager Email: {managerEmail}\nNew Hire Name: {newHireName}\nStart Date: {startDate}\nJob Title: {jobTitle}\nDesired Email for New Hire: {newHireEmail}\nDesired Email Lists: {emailLists}\nIs a new computer needed? {computerSelect}\n\nIs this information correct?"

        # If the user selects yes after reviewing the data, the program will then export the data.
        if messagebox.askyesno("Confirm data", confirmation_message):
            with open("newHireSheet.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Company Name", "Manager Name", "Manager E-mail", "New Hire Name", "Start Date", "Job Title",
                     "New Hire E-mail", "E-mail Lists", "Computer Selection"])
                writer.writerow([companyName,managerName,managerEmail,newHireName,startDate,jobTitle,newHireEmail,emailLists,computerSelect])
            messagebox.showinfo("New Hire Sheet Created.", " Form exported to newHireSheet.csv")

# main window
root = tk.Tk()
newHireProgram = newHireProgram(root)
root.mainloop()
