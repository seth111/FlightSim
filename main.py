import tkinter as tk
from controller.main_controller import MainController

if __name__ == "__main__":
    root = tk.Tk()
    app = MainController(root)
    app.run()
