import web

urls = (
    '/(.*)/(.*)', 'index'
)

app = web.application(urls, globals())

ROUTE_RENDER = "resources/"
render = web.template.render(ROUTE_RENDER)

class index:
    def GET(self, name, age):
        return render.main(name, age)
        #return '<html><h1> Hello {}.</h1> How are you today?</html>'.format(name)
        # To see this working go to a browser and paste: http://localhost:8080/Sergiyo


if __name__ == "__main__":
    app.run()