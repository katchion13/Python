from flask import Flask
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')
def index():
    return app.send_static_file('index.html')

app.run(port=https://katchion13.github.io/Python/, debug=True)
