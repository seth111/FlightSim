class ClientController:
    def __init__(self, view, user):
        self.view = view
        self.user = user

    def run(self):
        self.view.root.mainloop()
