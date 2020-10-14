from tkinter import *

window = Tk()
window.title('Temperature Convertor')
window.geometry('600x500')
window.configure(bg="yellow")


L1 = LabelFrame(window, text="Celcius To Fahrenheit", padx=40, pady=40, bg="pink")
L1.pack(fill="both")
L1.place(x=30, y=50)

E1 = Entry(L1, state='disable')
E1.pack()

L2 = LabelFrame(window, text="Fahrenheit to Celcius", padx=40, pady=40, bg="pink")
L2.pack(fill="both")
L2.place(x=310, y=50)

E2 = Entry(L2, state="disable")
E2.pack()


def activate_cel():
    E1.configure(state="normal")

btn1 = Button(window, text="Activate -Celcius to Fahrenheit", command=activate_cel)
btn1.place(x=30, y=250)


def activate_faren():
    E2.configure(state="normal")

btn2 = Button(window, text="Activate -Fahrenheit to Celcius", command=activate_faren)

btn2.place(x=330, y=250)


def exit():
    window.destroy()
exit_btn = Button(window, text = "Quit", command=exit)
exit_btn.place(x=500, y=430)


result_entry=Entry(window, bg="blue")
result_entry.place(x=220, y=330)


def Clear():
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0, END)
Clear_btn=Button(window, text="Clear", command=Clear)
Clear_btn.place(x=495, y=380)

def convert_to_C():
    if E1:
        fahrenheit = float(E1.get())
        celcius = (fahrenheit-32)*5/9
        result_entry.insert(0, celcius)

result_bnt = Button(window, text="Calculate C - F",command=convert_to_C)
result_bnt.place(x=30, y=330)

def convert_to_F():
    if E2:
        celcius = float(E2.get())
        fahrenheit = (celcius*9/5)+32
        result_entry.insert(0, fahrenheit)

result_bnt = Button(window, text="Calculate F - C",command=convert_to_F)
result_bnt.place(x=435, y=330)

window.mainloop()