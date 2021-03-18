# Practical 12
"""
This might not work here as this is running on a server. (No Display)
However, this can be run on any other computer with python, tcl and the tkinter module.
"""
from tkinter import messagebox, Tk, Label, Button, Entry
# the modules were listed seperately to improve execution time(less no. of
# imports)
wind = Tk()
wind.title('Simple Interest Calculator')
greet = Label(
    wind,
    text='Welcome to Simple Interest Calculator!').grid(
        row=0,
        column=0,
        columnspan=2,
         pady=6)
p_l = Label(wind, text='Enter Principal: ').grid(row=1, column=0)
r_l = Label(wind, text='Enter Rate: ').grid(row=2, column=0)
t_l = Label(wind, text='Enter time: ').grid(row=3, column=0)

p = Entry(wind)
p.grid(row=1, column=1)
r = Entry(wind)
r.grid(row=2, column=1)
t= Entry(wind)
t.grid(row=3, column=1)

def si():
    try:
        si_var = int(p.get()) * int(r.get()) * int(t.get()) / 100
        m = messagebox.showinfo("Simple interest", f'Simple Interest: {si_var}')
    except Exception as e:
        m= messagebox.showerror("ERROR!!!", e)
but= Button(wind, text= 'Calculate Simple Interest', command= si).grid(row= 4, column = 0, columnspan =2, pady= 5)

wind.mainloop()
