from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)

#docker run -p 8080:8080 flask-docker-app