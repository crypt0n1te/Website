from flask import Flask, render_template, request
from flask_assets import Environment, Bundle



app = Flask(__name__)

# the following preprocesses the scss files, converting them
# into regular (as well as minified) css files in /static/gen
assets = Environment(app)
assets.register({
    'home-css': Bundle(
        'css/home.scss',
        filters=('libsass', 'cssmin'),
        depends='css/*.scss',
        output='gen/home.%(version)s.min.css'),
})


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
