from tkinter import *
import math

def click(value):
    ex = entry_display.get()  # 789, ex[0:len(ex)-1]
    answer = ""

    try:

        if value == "C":
            ex = ex[0:len(ex)-1]  # 78
            entry_display.delete(0, END)
            entry_display.insert(0, ex)

        elif value == "CE":
            entry_display.delete(0, END)

        elif value == "√":
            answer = math.sqrt(eval(ex))

        elif value == "π":
            answer = math.pi

        elif value == "sin":
            answer = math.sin(math.radians(eval(ex)))

        elif value == "cos":
            answer = math.cos(math.radians(eval(ex)))

        elif value == "tan":
            answer = math.tan(math.radians(eval(ex)))

        elif value == "2π":
            answer = 2*math.pi

        elif value == "sinh":
            answer = math.sinh(eval(ex))

        elif value == "cosh":
            answer = math.cosh(eval(ex))

        elif value == "tanh":
            answer = math.tanh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex)**(1/3)

        elif value == "x\u02b8": #2**3=8
            entry_display.insert(END, "**")

        elif value == "x\u0083":
            answer = eval(ex)**3

        elif value == "x\u0082":
            answer == eval(ex)**2

        elif value == "ln":
            answer = math.log2(eval(ex))

        elif value == "deg":
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == "e":
            answer = math.e

        elif value == "x!":
            answer = math.factorial(eval(ex))

        elif value == chr(247):
            entry_display.insert(END, "/")
            return

        elif value == "=":
            answer = eval(ex)

        else:
            entry_display.insert(END, value)
            return

        entry_display.delete(0, END)
        entry_display.insert(0, answer)

    except SyntaxError:
        pass
        \

root = Tk()
root.title('Scientific Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

entry_display = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief='sunken', width=30)
entry_display.grid(row=0, column=0, columnspan=8)
button_text_list = ["C", "CE", "√", "+", "π", "sin", "cos", "tan",
                    "1", "2", "3", "-", "2π", "sinh", "cosh", "tanh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u0083", "x\u0082",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "(", ")", "x!"]
row_value = 1
column_value = 0

for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief='sunken', text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i:click(button))
    button.grid(row=row_value, column=column_value, pady=1)
    column_value += 1
    if column_value > 7:
        row_value += 1
        column_value = 0

root.mainloop()


