from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "localhost:27017"}
app.config["SECRET_KEY"] = "Shhh don't tell!"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from incidentreports.views import reports
    app.register_blueprint(reports)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
