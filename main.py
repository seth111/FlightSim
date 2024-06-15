import tkinter as tk
from view.main_view import MainView

def main():
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
