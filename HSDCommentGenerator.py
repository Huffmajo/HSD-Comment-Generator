from tkinter import *

# create window
window = Tk()
var = IntVar()
window.title("HSD Comment Generator")
# window.geometry("600x600")


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

# type of comment choices
radioComplete = Radiobutton(window, text="Completed", variable=var, value=1, command=selectRadio)
radioReworks = Radiobutton(window, text="Sent for reworks", variable=var, value=2, command=selectRadio)
radioOther = Radiobutton(window, text="Other", variable=var, value=3, command=selectRadio)
radioComplete.grid(column=0, row=1, sticky="w")
radioReworks.grid(column=0, row=6, sticky="w")
radioOther.grid(column=0, row=8, sticky="w")

# COMPLETE CHOICES
# reworks applied
checkAppliedState = BooleanVar()
checkAppliedState.set(False)
checkApplied = Checkbutton(window, text="Reworks applied", var=checkAppliedState)
checkApplied.grid(column=1, row=1, sticky="w")

entryApplied = Entry(window, width=40)
entryApplied.grid(column=2, row=1, sticky="w")
	
# flashed ifwi
checkIfwiState = BooleanVar()
checkIfwiState.set(False)
checkIfwi = Checkbutton(window, text="IFWI flashed", var=checkIfwiState)
checkIfwi.grid(column=1, row=2, sticky="w")	
	
# flashed ec
checkEcState = BooleanVar()
checkEcState.set(False)
checkEc = Checkbutton(window, text="EC flashed", var=checkEcState)
checkEc.grid(column=1, row=3, sticky="w")
	
# video outputs
checkVideoState = BooleanVar()
checkVideoState.set(False)
checkVideo = Checkbutton(window, text="Video outputs", var=checkVideoState)
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
generate = Button(window, text="Generate comment", width=80)
generate.grid(columnspan=2, column=0, row=10)

# Copy to clipboard button
copyButton = Button(window, text="Copy comment to clipboard", width=40)
copyButton.grid(columnspan=1, column=2, row=10)

# text generation field
generatedText = Text(window, width=120, height=10)
generatedText.grid(columnspan=3, column=0, row=11)


window.mainloop()