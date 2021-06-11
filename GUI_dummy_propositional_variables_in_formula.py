from tkinter import *
from tkinter import messagebox
from dummy_propositional_variables_in_formula import result


class GUIDummyPropositionalVariablesInFormula:
    def __init__(self):
        self.window = Tk()
        self.window['bg'] = '#ffe4c4'
        self.window.title("Dummy propositional variables in the formula")
        self.window.geometry('350x150')
        self.window.resizable(height=False, width=False)

        self.frame = Frame(self.window, bg='#ffe4c4')
        self.frame.place(relwidth=1, relheight=1)
        self.title = Label(self.frame, text='Enter formula', bg='#ffe4c4', font="Arial 16")
        self.title.pack()
        self.enterFormula = Entry(self.frame, width=45)
        self.enterFormula.pack()
        self.checkButton = Button(self.frame, text='Check', font="Arial 12", command=self.check)
        self.checkButton.pack()

        self.photo = PhotoImage(file="question_symbol.png")
        self.memoButton = Button(self.frame, image=self.photo, highlightthickness=0, bd=0, command=self.manual)
        self.memoButton.place(x=415, y=5)

        self.window.mainloop()

    def manual(self):
        def close():
            instructionWindow.destroy()

        instructionWindow = Toplevel()
        instructionWindow['bg'] = '#ffe4c4'
        instructionWindow.geometry('250x150')
        instructionWindow.title("Manual")
        instructionWindow.resizable(False, False)
        Label(instructionWindow, text="\/ - disjunction \n /\ - conjunction \n !- negation \n -> - implication \n"
                                      "\n ~ - equivalence \n [A...Z] - latin alphabet",
              font="Arial 12", bg='#ffe4c4').pack()

        closeButton = Button(instructionWindow, text='OK', font="Arial 12", command=close)
        closeButton.pack()

    def check(self):

        function = self.enterFormula.get()
        messagebox.showinfo("Результат", f"{result(function)}")

