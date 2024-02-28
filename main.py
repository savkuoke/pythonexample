import tkinter as tk
# import newer version of tkinter
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("PythonExample App")
    # sets window size to 600x400 and position to 50x50
    root.geometry('800x600+50+50')



# older classic theme
tk.Label(root, text='Classic Label').pack()
# newer theme
ttk.Label(root, text='Themed Label').pack()

root.mainloop()



if __name__ == "__main__":
    main()
