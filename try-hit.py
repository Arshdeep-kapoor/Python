#ques 8.10
'''
input="0"
global out
out = ""
def decimalToBinary(value):
    value=int(value)
    global out
    while value>0:
        r=value%2
        value//=2
        out=str(r)+out
    return out
print(decimalToBinary(input))           

deck=[]
deck=[x for x in range(52)]
deck=list(range(0,12))
print(deck)

lt=[10,1, 5, 16, 61, 9, 11, 1]
m=lt[0]
lt1,lt2,lt3=[],[],[]
for i in range(1,len(lt)):
    if lt[i]<=m:
        lt1.append(lt[i])
    else:
        lt2.append(lt[i])

lt3.extend(lt1)
lt3.append(m)
lt3.extend(lt2)
print(lt3)

lt=[eval(x) for x in list('232534312')]
count=10*[0]
for i in lt:
    count[i]+=1

#ifile = input("Enter the file name to count the words in it")
ifh = ['Cat','at','cAAt','cat']#open(ifile, "r")
count=0
count1=0
x={"A","E","I","O","U"}
#y={"B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"}
for i in ifh:
    words = i.strip()
    words = words.split(" ")
    print(words)
    for word in words:
        print(word)
        for letter in word:
            letter=letter.upper()
            print(letter)
            if letter in x:
                count=count+1
            else:#if letter in y:
                count1=count+1
            #else:
            #    continue
            print("The count is: ", count)
            print("The count1 is: ", count1)

print("The number of vowles are: ", count)
print("The number of Consonants are: ", count1)
print(lt,count)
'''
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