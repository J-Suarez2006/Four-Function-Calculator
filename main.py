import tkinter as tk
import evaluateStringExpression as es

root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")

label = tk.Label(root, text = "Calculator", font = ('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height = 3, font = ('Arial', 18))
textbox.pack(padx = 10)

def calculate():
    tocalculate = textbox.get('1.0', tk.END)
    result = es.evaluateAll(es.splitExpressionIntoArray(tocalculate))
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, result)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text = "1", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '1'))
btn1.grid(row = 0, column = 0, sticky = tk.W+tk.E)

btn2 = tk.Button(buttonframe, text = "2", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '2'))
btn2.grid(row = 0, column = 1, sticky = tk.W+tk.E)

btn3 = tk.Button(buttonframe, text = "3", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '3'))
btn3.grid(row = 0, column = 2, sticky = tk.W+tk.E)

btn4 = tk.Button(buttonframe, text = "4", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '4'))
btn4.grid(row = 1, column = 0, sticky = tk.W+tk.E)

btn5 = tk.Button(buttonframe, text = "5", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '5'))
btn5.grid(row = 1, column = 1, sticky = tk.W+tk.E)

btn6 = tk.Button(buttonframe, text = "6", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '6'))
btn6.grid(row = 1, column = 2, sticky = tk.W+tk.E)

btn7 = tk.Button(buttonframe, text = "7", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '7'))
btn7.grid(row = 2, column = 0, sticky = tk.W+tk.E)

btn8 = tk.Button(buttonframe, text = "8", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '8'))
btn8.grid(row = 2, column = 1, sticky = tk.W+tk.E)

btn9 = tk.Button(buttonframe, text = "9", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '9'))
btn9.grid(row = 2, column = 2, sticky = tk.W+tk.E)

btn0 = tk.Button(buttonframe, text = "0", padx = 5, pady = 5, font = ('Arial', 18),
                 command = lambda: textbox.insert(tk.END, '0'))
btn0.grid(row = 3, column = 0, sticky = tk.W+tk.E)

btnAdd = tk.Button(buttonframe, text = "+", padx = 5, pady = 5, font = ('Arial', 18),
                   command = lambda: textbox.insert(tk.END, '+'))
btnAdd.grid(row = 3, column = 1, sticky = tk.W+tk.E)

btnSub = tk.Button(buttonframe, text = "-", padx = 5, pady = 5, font = ('Arial', 18),
                   command = lambda: textbox.insert(tk.END, '-'))
btnSub.grid(row = 3, column = 2, sticky = tk.W+tk.E)

btnDiv = tk.Button(buttonframe, text = "/", padx = 5, pady = 5, font = ('Arial', 18),
                   command = lambda: textbox.insert(tk.END, '/'))
btnDiv.grid(row = 3, column = 3, sticky = tk.W+tk.E)

btnMult = tk.Button(buttonframe, text = "*", padx = 5, pady = 5, font = ('Arial', 18),
                    command = lambda: textbox.insert(tk.END, '*'))
btnMult.grid(row = 2, column = 3, sticky = tk.W+tk.E)

btnClear = tk.Button(buttonframe, text = "c", padx = 5, pady = 5, font = ('Arial', 18),
                     command = lambda: textbox.delete('1.0', tk.END))
btnClear.grid(row = 4, column = 3, sticky = tk.W+tk.E)

btnEquals = tk.Button(buttonframe, text = "=", padx = 5, pady = 5, font = ('Arial', 18),
                      command = calculate)
btnEquals.grid(row = 4, column = 2, sticky = tk.W+tk.E)

btnLeftPar = tk.Button(buttonframe, text = "(", padx = 5, pady = 5, font = ('Arial', 18),
                       command = lambda: textbox.insert(tk.END, '('))
btnLeftPar.grid(row = 4, column = 0, sticky = tk.W+tk.E)

btnRightPar = tk.Button(buttonframe, text = ")", padx = 5, pady = 5, font = ('Arial', 18),
                        command = lambda: textbox.insert(tk.END, ')'))
btnRightPar.grid(row = 4, column = 1, sticky = tk.W+tk.E)

btnExp = tk.Button(buttonframe, text = "^", padx = 5, pady = 5, font = ('Arial', 18),
                        command = lambda: textbox.insert(tk.END, '^'))
btnExp.grid(row = 1, column = 3, sticky = tk.W+tk.E)

buttonframe.pack(fill = 'x')

root.mainloop()