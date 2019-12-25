from flask import Flask, render_template

# setup app
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

