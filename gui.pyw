# coding=UTF-8

import sys
import tkinter
import tkinter.messagebox
from os import name as os_name

mainWindow = tkinter.Tk()
mainWindow.title("Force Calculator")
mainText = tkinter.Text(mainWindow)
mainText.pack()
mainText.insert("end", "# Define functions here\ndef ")
def doglobals() :
    exec("global "+", ".join(list(alllocals))+"\n"+mainText.get("1.0", "end"))
def define_func() :
    global mainText
    try :
        exec("global alllocals\n"+mainText.get("1.0", "end")+"\nalllocals = locals()\ndoglobals()")
    except BaseException as err :
        tkinter.messagebox.showerror("traceback", str(err))
    else :
        mainGlobals.configure(text="globals = "+repr(globals()))
        tkinter.messagebox.showinfo("Hint", "Defined successfully.")
mainDefine = tkinter.Button(mainWindow, text="Define", command=define_func)
mainDefine.pack()
mainGlobals = tkinter.Message(mainWindow, text="globals = "+repr(globals()))
mainGlobals.pack()
mainLabel = tkinter.Label(mainWindow, text="Input an expression:")
mainLabel.pack()
mainEntry = tkinter.Entry(mainWindow)
mainEntry.pack()
def calculate_eval() :
    global mainResult
    try :
        res = repr(eval(mainEntry.get()))
    except BaseException as err :
        tkinter.messagebox.showerror("traceback", str(err))
    else :
        mainResult.configure(text=res)
mainButton = tkinter.Button(mainWindow, text="Calculate", command=calculate_eval)
mainButton.pack()
mainResult = tkinter.Label(mainWindow, text="")
mainResult.pack()
mainWindow.mainloop()
