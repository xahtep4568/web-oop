from api import API

app = API()

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
