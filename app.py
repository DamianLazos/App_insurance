# ******************************PYTHON LIBRARIES******************************

# ******************************EXTERNAL LIBRARIES****************************
from flask import Flask
from dotenv import load_dotenv
from jinja2 import Environment
# ******************************OWN LIBRARIES*********************************
from config import AppConfiguration
from extensions import db, migrate
from src.models import *
from src.routes.units import blp as UnitsBlueprint
from src.routes.bussiness import blp as BusinessBlueprint
from src.routes.insurance import blp as InsuranceBlueprint
from src.routes.bus_ins import blp as BusinessInsuranceBlueprint
from src.routes.forms import blp as FormsBlueprint
from src.routes.export import blp as ExportBlueprint
# ***********************************CODE*************************************
def create_app():
    # Flask instance
    app = Flask(__name__)
    # App configuration
    app.config.from_object(AppConfiguration)
    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Registered blueprints
    app.register_blueprint(UnitsBlueprint)
    app.register_blueprint(BusinessBlueprint)
    app.register_blueprint(InsuranceBlueprint)
    app.register_blueprint(BusinessInsuranceBlueprint)
    app.register_blueprint(FormsBlueprint)
    app.register_blueprint(ExportBlueprint)

    # Database creation
    with app.app_context():
        db.create_all()
        
    # Template filters for Jinja2
    @app.template_filter(name="checker")
    def checker(value):
        if type(value) == list:
            return "lista"
        elif type(value) == dict:
            return "diccionario"
        elif type(value) == str:
            return "string"
        else:
            return "Tipo de dato desconocido"

    return app





