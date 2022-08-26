from program import app

@app.route('/')
def index():
    return "Hello, Dave."