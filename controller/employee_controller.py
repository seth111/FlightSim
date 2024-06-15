class EmployeeController:
    def __init__(self, view):
        self.view = view

    def run(self):
        self.view.root.mainloop()
