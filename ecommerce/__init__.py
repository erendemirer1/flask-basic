from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def createApp():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:130416@localhost:5432/ecommerce"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)

    return app
