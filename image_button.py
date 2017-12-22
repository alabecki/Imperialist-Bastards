
from appJar import gui


def fun(btn):
	print("Function working!!: %s", btn)

def fun2(btn):
	app.disableButton("crown2")
	print("Fun2! Twice the fun!")

def try_this(btn):
	print("Lets see if this works...")


app = gui("Image Button")
app.setIcon("crown.gif")
app.setFont("11", "arial")
app.setExpand("all")
app.setPadding([1, 1])
app.setInPadding([2, 2])

app.startTabbedFrame("GameGUI")
	
app.startTab("MainTab")

#app.addButton("push", none)
app.addImage("crown", "crown.gif")
app.setImageSubmitFunction("crown", fun)

app.addImageButton("crown2", fun2, "crown.gif")
app.setButtonTooltip("crown2", "Crown")

app.addMessage("message", "Here is some text")
app.setMessageBg("message", "green")

app.stopTab()

app.startTab("Try This")
app.startLabelFrame("Frame")
app.addLabel("1", "ONE: ", 1, 1)
app.addLabel("11", "%d" % 1, 1, 2)
app.setLabelRelief("11", "sunken")
app.addLabel("2", "TWO")
app.setLabelRelief("1", "raised")
app.addLabel("3", "THREE")
app.setLabelRelief("1", "groove")
app.addLabel("4", "FOUR")
app.setLabelRelief("1", "ridge")
app.addLabel("5", "FIVE")
app.setLabelRelief("1", "flat")
app.stopLabelFrame()
app.stopTab()

app.stopTabbedFrame()



app.go()