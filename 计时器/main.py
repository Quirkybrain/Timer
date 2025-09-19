import tkinter as tk
import MainPage

root = tk.Tk()
root.title("Timer")
root.geometry("900x300+500+400")
app = MainPage.Clock(master=root)
root.mainloop()
