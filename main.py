from kivymd.app import MDApp
from kivymd.uix.label import label

import tkinter as tk
from time import strftime

class Main_App(MDApp):
  def build(self):
    #return label.MDLabel(text="Hello world", halign="center")
    window=tk.Tk()
    window.title("My Digital CLock")
    window.geometry("300x400")
    window.config(bg="Blue")

    label=tk.Label(window, font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
    #label.place(x=50, y=50, height=200, width=200)
    label.pack(anchor="center")

    def time():
      string=strftime("%H:%M:%S %p")
      label.config(text=string)
      label.after(1000, time)

    time()

    window.mainloop()

if __name__ == "__main__":
  Main_App().run()
  