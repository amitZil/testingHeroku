from flask import Flask
from API.PredictService import PredictService
from OnBoarding.DataInsert import DataInsertService

application = Flask(__name__)
application.register_blueprint(PredictService.PredictServiceBluePrint)
application.register_blueprint(DataInsertService.DataInsertServiceBlueprint)

if __name__ == '__main__':
    application.run()