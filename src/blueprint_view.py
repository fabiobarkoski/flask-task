from flask import Blueprint
from flask import request
import numpy as np
from numpy.lib.shape_base import split
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

def calc_distance(lat1,lat2,lon1,lon2):
    r = 6371
    dlat = np.deg2rad(lat2 - lat1)
    dlon = np.deg2rad(lon2 - lon1)
    a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.deg2rad(lat1)) * np.cos(np.deg2rad(lat2)) * np.sin(dlon/2) * np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = r * c
    return round(d)
 

@distance_bp.route('/', methods=['GET'])
def distante():
    coordinate1 = request.args.get('from')
    coordinate2 = request.args.get('to')
    list1 = []
    list2 = []

    if ',' in coordinate1:
        coord1_list = coordinate1.split(',')
        list1.append(coord1_list[0])
        list1.append(coord1_list[1])
    else:
        r1 = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{coordinate1}.json?access_token=pk.eyJ1IjoiYmZhYmlvIiwiYSI6ImNrc2txaWQzeTExcW0ybm85cG9nNzd1ZjgifQ.bTBrNVZt0YFEDn-7YZIk_w')
        response1 = r1.json()
        list1.append(response1['features'][0]['center'][0])
        list1.append(response1['features'][0]['center'][1])

    if ',' in coordinate2:
        coord2_list = coordinate2.split(',')
        list2.append(coord2_list[0])
        list2.append(coord2_list[1])    
    else:
        r2 = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{coordinate2}.json?access_token=pk.eyJ1IjoiYmZhYmlvIiwiYSI6ImNrc2txaWQzeTExcW0ybm85cG9nNzd1ZjgifQ.bTBrNVZt0YFEDn-7YZIk_w')
        response2 = r2.json()
        list2.append(response2['features'][0]['center'][0])
        list2.append(response2['features'][0]['center'][1])


    save = str((calc_distance(float(list1[1]), float(list2[1]), float(list1[0]), float(list2[0]))))

    logger.info(f'The distance from {coordinate1} to {coordinate2} is {save} km')
    return save