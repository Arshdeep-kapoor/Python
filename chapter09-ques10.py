from tkinter import *

class PieChart:
    def __init__(self,master):
        master.title("Tk - Pie Chart")
        
        self.canvas = Canvas(master,width = 400,height = 400 )
        self.canvas.pack()
        
        self.Arc1 = self.canvas.create_arc(100,100,300,300,start = 0,extent = 72,fill="red")
        self.Arc2 = self.canvas.create_arc(100,100,300,300,start = 72,extent = 36,fill="blue")
        
        self.Arc3 = self.canvas.create_arc(100,100,300,300,start = 108,extent = 108,fill="green")
        self.Arc1 = self.canvas.create_arc(100,100,300,300,start = 216,extent = 144,fill="orange")
        
        self.txt1 = self.canvas.create_text(280,150,text="Project -- 20%")
        self.txt2 = self.canvas.create_text(200,100,text="Quizes -- 10%")
        self.txt3 = self.canvas.create_text(90,190,text="Midterm -- 30%")
        self.txt4 = self.canvas.create_text(245,290,text="Final -- 40%")
        
window = Tk()
p = PieChart(window)
window.mainloop()