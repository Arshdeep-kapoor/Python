from tkinter import *
da = 10
db = 10
dc = 10
dd = 10
class panel:
    
    def __init__(self):
        self.radius = 10
        window = Tk()
        window.title("Moving Ball")
        
        self.canvas = Canvas(window,width=200,height=200,bg="white")
        self.canvas.pack()
        
        self.canvas.create_oval(90,90,110,110,fill="red",tag = "ball")
        frame = Frame(window)
        frame.pack()
        btLeft = Button(frame, text="Left",command=self.moveLeft)
        btRight = Button(frame, text="Right",command=self.moveRight)
        btUp = Button(frame, text="Up",command=self.moveUp)
        btDown = Button(frame, text="Down",command=self.moveDown)
        
        btLeft.grid(row=1,column=1)
        btRight.grid(row=1,column=2)
        btUp.grid(row=1,column=3)
        btDown.grid(row=1,column=4)
        
        
        window.mainloop()
        
    def moveLeft(self):
        global da
        self.canvas.delete("ball")
        self.canvas.create_oval(90-da,90,110-da,110,fill="red",tag = "ball")
        if (da <=90):
            da+=10
                    
    def moveRight(self):
        global db
        self.canvas.delete("ball")
        self.canvas.create_oval(130+db,90,110+db,110,fill="red",tag = "ball")
        if (db<=90):
            db+=10
        
    def moveUp(self):
        global dc
        self.canvas.delete("ball")
        self.canvas.create_oval(90,60-dc,110,80-dc,fill="red",tag = "ball")
        if (dc<=90):
            dc+=10
        
    def moveDown(self):
        global dd
        self.canvas.delete("ball")
        self.canvas.create_oval(90,120+dd,110,140+dd,fill="red",tag = "ball")
        if(dd<=90):
            dd+=10
        
panel()