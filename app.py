from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/art work')
def on_login():
    return render_template('login.html')

@app.route('/talent')
def talent():
    return render_template('Talent.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/testing')
def test():
    return render_template('testing.html')

if __name__ == "__main__":
    app.run(debug=True, port=2048)