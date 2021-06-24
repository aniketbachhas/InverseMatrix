from tkinter import *
import numpy as np

def inverse():
    matrix = np.array([[int(e1.get()), int(e2.get()), int(e3.get())],
                       [int(e4.get()), int(e5.get()), int(e6.get())],
                       [int(e7.get()), int(e8.get()), int(e9.get())]])
    res = np.linalg.inv(matrix)
    text = Label(root, text="Inverse of matrix is:")
    text.grid(row = 7, column = 0, columnspan = 3)
    for i in range(3):
        for j in range(3):
            result = Label(root, text=res[i][j])
            result.grid(row = i+8, column = j)

root = Tk()
root.title("Matrix Inverse Calculator")

myLabel = Label(root, text="Enter Matrix:")
myLabel.grid(row = 0, column = 0, columnspan = 3)

e1 = Entry(root, width = 5, borderwidth = 1)
e1.grid(row = 1, column = 0)
e2 = Entry(root, width = 5, borderwidth = 1)
e2.grid(row = 1, column = 1)
e3 = Entry(root, width = 5, borderwidth = 1)
e3.grid(row = 1, column = 2)
e4 = Entry(root, width = 5, borderwidth = 1)
e4.grid(row = 2, column = 0)
e5 = Entry(root, width = 5, borderwidth = 1)
e5.grid(row = 2, column = 1)
e6 = Entry(root, width = 5, borderwidth = 1)
e6.grid(row = 2, column = 2)
e7 = Entry(root, width = 5, borderwidth = 1)
e7.grid(row = 3, column = 0)
e8 = Entry(root, width = 5, borderwidth = 1)
e8.grid(row = 3, column = 1)
e9 = Entry(root, width = 5, borderwidth = 1)
e9.grid(row = 3, column = 2)



calc = Button(root, text="Calculate Inverse", command=inverse)
calc.grid(row = 5, column = 0, columnspan = 3)


root.mainloop()