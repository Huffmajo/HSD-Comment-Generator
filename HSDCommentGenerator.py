from tkinter import *

# create window
window = Tk()
window.title("HSD Comment Generator")
window.geometry("600x600")


# type of comment prompt
labelCommentPrompt = Label(window, text="Comment Generator", font=("Helvetica", 20))
labelCommentPrompt.grid(column=0, row=0)

# type of comment choices
radioComplete = Radiobutton(window, text="Completed", value=1)
radioReworks = Radiobutton(window, text="Sent for reworks", value=2)
radioOther = Radiobutton(window, text="Other", value=3)
radioComplete.grid(column=0, row=1)
radioReworks.grid(column=1, row=1)
radioOther.grid(column=2, row=1)

# reworks applied
checkAppliedState = BooleanVar()
checkAppliedState.set(False)
checkApplied = Checkbutton(window, text="Reworks applied", var=checkAppliedState)
checkApplied.grid(column=0, row=1)

entryApplied = Entry(window, width=40)
entryApplied.grid(column=1, row=1)
	
# flashed ifwi
checkIfwiState = BooleanVar()
checkIfwiState.set(False)
checkIfwi = Checkbutton(window, text="IFWI flashed", var=checkIfwiState)
checkIfwi.grid(column=0, row=2)	
	
# flashed ec
checkEcState = BooleanVar()
checkEcState.set(False)
checkEc = Checkbutton(window, text="EC flashed", var=checkEcState)
checkEc.grid(column=0, row=3)
	
# video outputs
checkVideoState = BooleanVar()
checkVideoState.set(False)
checkVideo = Checkbutton(window, text="Video outputs", var=checkVideoState)
checkVideo.grid(column=0, row=4)
	
entryVideo = Entry(window, width=40)
entryVideo.grid(column=1, row=4)

# show form for reworks style comment
# ticket number
labelReworkTicketNumber = Label(window, text="Rework ticket number")
labelReworkTicketNumber.grid(column=0, row=5)

entryReworkTicketNumber = Entry(window, width=40)
entryReworkTicketNumber.grid(column=1, row=5)


# show form for one-offs
# first one-off
labelOther = Label(window, text="One-offs will go here")
labelOther.grid(column=0, row=6)

# text generation field
labelGeneratedText = Label(window, text="Generated comment")
labelGeneratedText.grid(column=0, row=7)
generatedText = Entry(window, width=40)
generatedText.grid(column=1, row=7)

# generate button
generate = Button(window, text="Generate comment")
generate.grid(column=0, row=8)

window.mainloop()