from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
