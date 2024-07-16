# Python Calculator using tkinter to display it


from tkinter import *

def button_press(num):  #This helps to display all the typed numbers,signs,etc

    global equation_text
    
    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:                                   # For divide by 0 or some sort of complex number results etc

        total = str(eval(equation_text))   # eval parse the expression we pass in!

        equation_label.set(total)          # To execute the function

        equation_text = total              # reuse the total again

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")  # This shows the  output on the small window created where the number shown are showed!

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")                   # To effectively erase things on the shown calculator

    equation_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("500x500")                  # This creats window of height and width of 500 by 500(no gap w/'x')

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)                      #frame is used inorder to hold all the buttons and stuff in the output program!
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,   # Different text,height,width,font is selected to be displayed on the button 
                 command=lambda: button_press(1))  #command fucntion is used in order to execute the fucntion after typing the given number
button1.grid(row=0, column=0)             # this sets as to where the button should be located

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)  #different command 
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear) #instead of backspace 'clear' command is used
clear.pack()

window.mainloop()