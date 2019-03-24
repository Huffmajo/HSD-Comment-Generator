from tkinter import *

# create window
window = Tk()
window.title("HSD Comment Generator")
# window.geometry("600x600")

# vars for radio and check buttons
var = IntVar()
varApplied = IntVar()
varIFWI = IntVar()
varEC = IntVar()
varVideo = IntVar()

# type of comment prompt
labelCommentType = Label(window, text="1. Choose comment type ", font=("Helvetica, 14"))
labelCommentType.grid(column=0, row=0, sticky="w")
labelCommentSelect = Label(window, text="2. Choose subfields ", font=("Helvetica, 14"))
labelCommentSelect.grid(column=1, row=0, sticky="w")
labelCommentEntry = Label(window, text="3. Enter info ", font=("Helvetica, 14"))
labelCommentEntry.grid(column=2, row=0, sticky="w")

def selectRadio():
	# allow complete fields
	if var.get() == 1:
		checkApplied.config(state=NORMAL)
		entryApplied.config(state=NORMAL)
		checkIfwi.config(state=NORMAL)
		checkEc.config(state=NORMAL)
		checkVideo.config(state=NORMAL)
		entryVideo.config(state=NORMAL)
		entryReworkTicketNumber.config(state=DISABLED)
	
	# allow rework fields
	elif var.get() == 2:
		checkApplied.config(state=DISABLED)
		entryApplied.config(state=DISABLED)
		checkIfwi.config(state=DISABLED)
		checkEc.config(state=DISABLED)
		checkVideo.config(state=DISABLED)
		entryVideo.config(state=DISABLED)
		entryReworkTicketNumber.config(state=NORMAL)
	
	# allow other fields
	elif var.get() == 3:
		checkApplied.config(state=DISABLED)
		entryApplied.config(state=DISABLED)
		checkIfwi.config(state=DISABLED)
		checkEc.config(state=DISABLED)
		checkVideo.config(state=DISABLED)
		entryVideo.config(state=DISABLED)
		entryReworkTicketNumber.config(state=DISABLED)
	else:
		print("Something went wrong")

def createComment():
	# delete all text in comment field
	generatedText.delete(1.0, END)

	# create complete comment
	if var.get() == 1:
		comment = "***COMPLETE***\n"

		# add applied reworks if checked
		if varApplied.get() == 1:

			# add applied reworks if the field isn't empty
			if entryApplied.get() != "":
				reworks = entryApplied.get()
				comment += "Reworks %s applied\n" % reworks
			else:
				comment += "Required reworks applied\n"
		else:
			comment += "Up-to-date on required reworks\n"

		# add IFWI and EC messages based on checks
		if varIFWI.get() == 1:
			if varEC.get() == 1:
				comment += "IFWI and EC flashed\n"
			else:
				comment += "IFWI flashed\n"
		elif varEC.get() == 1:
			comment += "EC flashed\n"

		# add video outputs if checked
		if varVideo.get() == 1:
			comment += "Boots to shell"
			if entryVideo.get() != "":
				video = entryVideo.get()
				comment += ", video through %s\n" % video
			else:
				comment += "\n"

		# ending text
		comment += "Records updated in ISMP\nReady for pickup at HF1 inventroy cage\n"
	
	# create rework comment
	elif var.get() == 2:
		comment = "Submitted for required reworks"
		if entryReworkTicketNumber.get() != "":
			ticketNum = entryReworkTicketNumber.get()
			comment += " https://linkgoeshere.com/%s\n" % ticketNum
		else:
			comment += "\n"

	# create other comment
	elif var.get() == 3:
		comment = "Other comments go here\n"
	
	# no comment type was selected
	else:
		comment = "No comment type selected\n"

	# populate created comment to form
	generatedText.insert(INSERT, comment)

def copyToClipboard():
	copyText = generatedText.get()
	window.clipboard_clear()
	window.clipboard_append("copyText")

# type of comment choices
radioComplete = Radiobutton(window, text="Completed", variable=var, value=1, command=selectRadio)
radioReworks = Radiobutton(window, text="Sent for reworks", variable=var, value=2, command=selectRadio)
radioOther = Radiobutton(window, text="Other", variable=var, value=3, command=selectRadio)
radioComplete.grid(column=0, row=1, sticky="w")
radioReworks.grid(column=0, row=6, sticky="w")
radioOther.grid(column=0, row=8, sticky="w")

# COMPLETE CHOICES
# reworks applied
checkApplied = Checkbutton(window, text="Reworks applied", variable=varApplied)
checkApplied.grid(column=1, row=1, sticky="w")

entryApplied = Entry(window, width=40)
entryApplied.grid(column=2, row=1, sticky="w")
	
# flashed ifwi
checkIfwi = Checkbutton(window, text="IFWI flashed", variable=varIFWI)
checkIfwi.grid(column=1, row=2, sticky="w")	
	
# flashed ec
checkEc = Checkbutton(window, text="EC flashed", variable=varEC)
checkEc.grid(column=1, row=3, sticky="w")
	
# video outputs
checkVideo = Checkbutton(window, text="Video outputs", variable=varVideo)
checkVideo.grid(column=1, row=4, sticky="w")
	
entryVideo = Entry(window, width=40)
entryVideo.grid(column=2, row=4, sticky="w")

# REWORK CHOICES
# ticket number
labelReworkTicketNumber = Label(window, text="Rework ticket number")
labelReworkTicketNumber.grid(column=1, row=6, sticky="w")

entryReworkTicketNumber = Entry(window, width=40)
entryReworkTicketNumber.grid(column=2, row=6, sticky="w")


# OTHER choices
# first one-off
labelOther = Label(window, text="One-offs will go here")
labelOther.grid(columnspan=2, column=1, row=8)

# generate button
generate = Button(window, text="Generate comment", width=80, command=createComment)
generate.grid(columnspan=2, column=0, row=10)

# Copy to clipboard button
copyButton = Button(window, text="Copy comment to clipboard", width=40, command=copyToClipboard)
copyButton.grid(columnspan=1, column=2, row=10)

# text generation field
generatedText = Text(window, width=120, height=10)
generatedText.grid(columnspan=3, column=0, row=11)


window.mainloop()