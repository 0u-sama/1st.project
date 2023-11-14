from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("matplot")
root.geometry("400x200")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.pie(house_prices)
    plt.show()


Button(root, text="graphic", command=graph).pack()


root.mainloop()