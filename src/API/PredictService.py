from flask import Blueprint
from DB import DBLayer
from Auth import Auth


class PredictService:
    PredictServiceBluePrint = Blueprint('PredictService', 'PredictService')

    @staticmethod
    @PredictServiceBluePrint.route('/predict', methods=['GET', 'POST'])
    @Auth.auth.login_required
    def predict():
        mydb = DBLayer.get_DB()
        return mydb.sample_query('dad')

