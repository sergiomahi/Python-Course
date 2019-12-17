import web   
from Models import RegisterModel, LoginModel

urls = (
    '/', 'home',
    '/login', 'login',
    '/register', 'register',
    '/postregistration', 'postRegistration',
    '/check-login', 'checkLogin'
    
)

TEMPLATE_PATH = './Views/Templates'
BASE_FILE = 'MainLayout'

app = web.application(urls, globals())
render = web.template.render(TEMPLATE_PATH, base=BASE_FILE)
# Classes/Routes

class home:
    def GET(self):
        return render.home()

class login:
    def GET(self):
        return render.login()

class checkLogin:
    def POST(self):
        data = web.input()

        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_user(data)

        if isCorrect:
            return isCorrect

        return "error"

class register:
    def GET(self):
        return render.register()

class postRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username

if __name__ == "__main__":
    app.run()