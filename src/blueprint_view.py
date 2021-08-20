from flask import Blueprint
import requests
import logging

#configuring the log
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename='distance.log',
                    filemode='a',
                    level=logging.INFO,
                    format=log_format)

logger = logging.getLogger('root')                    

distance_bp = Blueprint('distance_bp', __name__)

@distance_bp.route('/<request>')
def distante(request):
    request_formated = request.replace(' ', '+')

    r = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{request_formated}.json?access_token=pk.eyJ1IjoiYmZhYmlvIiwiYSI6ImNrc2txaWQzeTExcW0ybm85cG9nNzd1ZjgifQ.bTBrNVZt0YFEDn-7YZIk_w')
    
    response = r.json()

    logger.info(response['features'][0]['center'])
    return "registrado :)"