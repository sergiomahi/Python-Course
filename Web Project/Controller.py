import web   

urls = (
    '/', 'home',
    '/register', 'register',
    '/postregistration', 'postRegistration'
)

TEMPLATE_PATH = './Views/Templates'
BASE_FILE = 'MainLayout'

app = web.application(urls, globals())
render = web.template.render(TEMPLATE_PATH, base=BASE_FILE)
# Classes/Routes

class home:
    def GET(self):
        return render.home()

class register:
    def GET(self):
        return render.register()

class postRegistration:
    def POST(self):
        data = web.input()
        return data.username

if __name__ == "__main__":
    app.run()