import tkinter as tk
from controller.main_controller import MainController
from view.main_view import MainView

def main():
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainController(root)
    app.run()
