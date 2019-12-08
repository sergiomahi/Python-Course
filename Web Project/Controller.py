import web   

urls = (
    '/', 'home'
)

TEMPLATE_PATH = './Views/Templates'
BASE_FILE = 'MainLayout'

app = web.application(urls, globals())
render = web.template.render(TEMPLATE_PATH, base=BASE_FILE)
# Classes/Routes

class home:
    def GET(self):
        return render.home()

if __name__ == "__main__":
    app.run()