from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/ab/<int:n>&<string:name>')
def index(n,name):
    return "welcome "+str(n)+name

if __name__ == "__main__":
    app.run(debug=True)