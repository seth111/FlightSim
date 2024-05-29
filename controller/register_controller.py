from view.register_view import RegisterView

class RegisterController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.register_view = RegisterView(self)

    def show_register(self):
        self.register_view.show()
