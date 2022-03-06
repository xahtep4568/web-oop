from api import API

app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"

@app.route("/hello/{name}")
def hello(request, response, name):
    response.text = f"Hello, {name}"

@app.route("/tell/{age:d}")
def tell(request, response, age):
    response.text = f"Your age, {age}"

@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"

@app.route("/diff/{num_1:d}/{num_2:d}")
def diff(request, response, num_1, num_2):
    total = int(num_1) - int(num_2)
    response.text = f"{num_1} - {num_2} = {total}"