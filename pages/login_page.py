class LoginPage:
    def __init__(self, page):
        self.page= page
        self.username= page.get_by_label("Username or Email")
        self.password = page.get_by_label("Password")
        self.loginuser = page.get_by_test_id("login-submit-button")
        self.error_message = page.get_by_test_id("login-error-message")


    def open(self):
        self.page.goto("https://qademo.com/login")

    def login(self, username , password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginuser.click()
