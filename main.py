import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("BMI Calculater")
window.minsize(width=300, height=300)

def bmi_calculate():
    kg=(w_entry.get())
    h=(h_entry.get())
    bmi =float(kg) /float(h) ** 2
    result_string= result(bmi)
    result_label.config(text=result_string)


weight_label=tkinter.Label(text="Enter your weight(kg)", font=("Calibri", 12, "bold"))
weight_label.config(bg="black", fg="white")
weight_label.pack(padx=10, pady=10)

w_entry=tkinter.Entry(width=30)
w_entry.pack(padx=5, pady=5)

height_label=tkinter.Label(text="Enter your height(kg)", font=("Calibri", 12, "bold"))
height_label.config(bg="black", fg="white")
height_label.pack(padx=20, pady=20)

h_entry=tkinter.Entry(width=30)
h_entry.pack(padx=5,pady=5)

clt_button=tkinter.Button(text="Calculate", command=bmi_calculate)
clt_button.pack()


result_label=tkinter.Label()
result_label.pack(padx=10,pady=10)

def result(bmi):
    resul_string=f"Your BMI is: {bmi}, type is:"
    if bmi < 18.5:
       resul_string += "Underweight"
    elif (bmi > 18.5) and (bmi < 24.9):
       resul_string +="Normal"
    elif (bmi > 24.9) and (bmi < 29.9):
        resul_string +="Overweight"
    elif (bmi > 29.9):
        resul_string +="Obesity"
    else:
        print("Enter your weight and height")
    return resul_string


window.mainloop()