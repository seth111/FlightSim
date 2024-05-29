from view.login_view import LoginView

class LoginController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.login_view = LoginView(self)

    def show_login(self):
        self.login_view.show()
