from tkinter import *


class InvestmentCalculator:
    def __init__(self,master):
        master.title("Tk - Investment Calculator")
        
        self.label1 = Label(master,text="Investment Amount:")
        self.label2 = Label(master,text="Years:")
        self.label3 = Label(master,text="Annual Interest Rate:")
        self.label4 = Label(master,text="Future Value:")
        
        self.I = StringVar()
        self.Y = StringVar()
        self.A = StringVar()
        self.F = StringVar()
        
        self.entry1=Entry(master,textvariable =self.I,justify = RIGHT )
        self.entry2=Entry(master,textvariable =self.Y,justify = RIGHT )
        self.entry3=Entry(master,textvariable =self.A,justify = RIGHT )
        self.entry4=Entry(master,textvariable =self.F,justify = RIGHT )
        
        self.buttonCalculate = Button(master,text="Calculate", command = self.CalculateFutureValue)
        
        self.label1.grid(row =0,sticky =W)
        self.label2.grid(row =1,sticky =W)
        self.label3.grid(row =2,sticky =W)
        self.label4.grid(row =3,sticky =W)
        
        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=1,column=1)
        self.entry3.grid(row=2,column=1)
        self.entry4.grid(row=3,column=1)
        
        self.buttonCalculate.grid(row=4,column=1,sticky=E)
    
    def CalculateFutureValue(self):
        FutureValue = float(self.I.get()) * (1 + float(self.A.get())/1200) **(int(self.Y.get()) *12)
        self.F.set(format(FutureValue,"10.2f"))
        
window = Tk()
I = InvestmentCalculator(window)  
window.mainloop()