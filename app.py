from api import API

app = API()


@app.route("/home")
def handler(req, resp):
    resp.body = app.template(
        "home.html",
        context={"title": "Awesome Framework", "name": "Bumbo"}
    )

@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html",
        context={"name": "Bumbo", "title": "Best Framework"}
    ).encode()

@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Endpoint to create a book"

    def put(self, req, resp):
        resp.text = "Endpoint to put a book"

    def delete(self, req, resp):
        resp.text = "Endpoint to delete a book"
