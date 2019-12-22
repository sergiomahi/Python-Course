import web   
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = (
    '/', 'home',
    '/login', 'login',
    '/register', 'register',
    '/postregistration', 'postRegistration',
    '/check-login', 'checkLogin',
    '/logout', 'logout',
    '/post-activity', 'postActivity'
    
)

TEMPLATE_PATH = './Views/Templates'
BASE_FILE = 'MainLayout'


app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render(TEMPLATE_PATH, base=BASE_FILE, globals={'session': session_data, 'current_user': session_data["user"]})
# Classes/Routes

class home:
    def GET(self):
        # Autologin.
        data = type('obj', (object,), {"username": "sergiomahi", "password": "sergiomahi"}) 

        login = LoginModel.LoginModel()

        isCorrect = login.check_user(data)
        if isCorrect:
            session_data["user"] = isCorrect

        post_model = Posts.Posts()
        all_posts = post_model.get_all_posts()


        return render.home(all_posts)

class login:
    def GET(self):
        return render.login()

class checkLogin:
    def POST(self):
        data = web.input()

        login_model = LoginModel.LoginModel()
        isCorrect = login_model.check_user(data)

        if isCorrect:
            session_data["user"]=isCorrect
            return isCorrect

        return "error"

class logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"

class register:
    def GET(self):
        return render.register()

class postRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username

class postActivity:
    def POST(self):
        data = web.input()
        data['username'] = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)

        return "success"
    
    
        

if __name__ == "__main__":
    app.run()