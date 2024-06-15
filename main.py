import tkinter as tk
<<<<<<< HEAD
from controller.main_controller import MainController
=======
from view.main_view import MainView

def main():
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
>>>>>>> 6b29119bf6201e84f2384f23da537268e1c125a9

if __name__ == "__main__":
    root = tk.Tk()
    app = MainController(root)
    app.run()
