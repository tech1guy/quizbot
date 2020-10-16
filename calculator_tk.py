import parser
from tkinter import *

root = Tk()

#Get Values
i = 0
def getVal(num):
    global i
    screen.insert(i, num)
    i += 1
    

def delVal():
    screen.delete(0,END)

#Get Operatorso

def getOperators(operator):
    global i 
    length = len(operator)
    screen.insert(i,operator)
    i += length

def calculate():

    allEntry = screen.get()
    try:
        x = parser.expr(allEntry).compile()
        result = eval(x)
        delVal()
        screen.insert(0,result)
    except Exception:
        delVal()
        screen.insert(0, "Invalid Input")





root.title("CALCULATOR")
root.minsize(width=305, height=155)
root.maxsize(width=305, height=155)

#Display Screen
screen = Entry(root, font=24, bd=5)
screen.grid(row=0, columnspan=6, sticky=W+E)

#Adding Buttons
Button(root, text="1", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(1)).grid(row=1, column =0)
Button(root, text="2", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(2)).grid(row=1, column =1)
Button(root, text="3", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(3)).grid(row=1, column =2)


Button(root, text="4", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(4)).grid(row=2, column =0)
Button(root, text="5", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(5)).grid(row=2, column =1)
Button(root, text="6", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(6)).grid(row=2, column =2)

Button(root, text="7", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(7)).grid(row=3, column =0)
Button(root, text="8", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(8)).grid(row=3, column =1)
Button(root, text="9", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(9)).grid(row=3, column =2)



Button(root, text="0", bg="#234", fg="#fff", width=5, bd=5, command= lambda: getVal(0)).grid(row=4, column =0)
Button(root, text=".", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators(".")).grid(row=4, column =1)
Button(root, text="=", bg="green", fg="#fff", width=5, bd=5, command=calculate).grid(row=4, column =2)

#Basic Operators
Button(root, text="+", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("+")).grid(row=1, column =3)
Button(root, text="-", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("-")).grid(row=2, column =3)
Button(root, text="*", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("*")).grid(row=3, column =3)
Button(root, text="/", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("/")).grid(row=4, column =3)


#More Operators
Button(root, text="^2", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("**2")).grid(row=1, column =4)
Button(root, text="%", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("%")).grid(row=2, column =4)
Button(root, text="(", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("(")).grid(row=3, column =4)
Button(root, text="Exp", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("**")).grid(row=4, column =4)

Button(root, text="AC", bg="brown", fg="#fff", width=5, bd=5, command=delVal).grid(row=1, column =5,)
Button(root, text="<-", bg="brown", fg="#fff", width=5, bd=5).grid(row=2, column =5,)
Button(root, text=")", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators(")")).grid(row=3, column =5)
Button(root, text="pi", bg="#234", fg="#fff", width=5, bd=5, command= lambda:getOperators("*3.14")).grid(row=4, column =5)


root.mainloop()
