from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/countries')
def countries():
    # countries.html contains the gallery and links to the static stylesheet
    return render_template('countries.html')


if __name__ == '__main__':
    app.run(debug=True)