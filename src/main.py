from flask import Flask
from API.PredictService import PredictService

application = Flask(__name__)
application.register_blueprint(PredictService.PredictServiceBluePrint)