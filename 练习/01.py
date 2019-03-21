from tkinter import *

class Application(Frame):
    def __init__(self):
        Frame.__init__(self,)
        self.pack()
        self.creteWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello,world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text ='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()

app.master.title('Hello Wrold')

app.mainloop()