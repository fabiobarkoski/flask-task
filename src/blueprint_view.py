from flask import Blueprint
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Feature
from mkad_polygon import polygon
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
 

@distance_bp.route('/<coordinate>', methods=['GET'])
def distante(coordinate):
    list1 = [37.842762,55.774558]
    list2 = []

    bol = 0

    if ',' in coordinate:
        coord_list = coordinate.split(',')      
        list2.append(coord_list[0])
        list2.append(coord_list[1])
        point = Feature(geometry=Point((float(list2[0]), float(list2[1]))))
        print(boolean_point_in_polygon(point, polygon))
        if boolean_point_in_polygon(point, polygon) == True:
            bol +=1
        
    else:
        r = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{coordinate}.json?access_token=pk.eyJ1IjoiYmZhYmlvIiwiYSI6ImNrc2txaWQzeTExcW0ybm85cG9nNzd1ZjgifQ.bTBrNVZt0YFEDn-7YZIk_w')
        response = r.json()
        list2.append(response['features'][0]['center'][0])
        list2.append(response['features'][0]['center'][1])
        point = Feature(geometry=Point((float(list2[0]), float(list2[1]))))
        print(boolean_point_in_polygon(point, polygon))
        if boolean_point_in_polygon(point, polygon) == True:
            bol +=1

    save = str((calc_distance(float(list1[1]), float(list2[0]), float(list1[0]), float(list2[1]))))

    if bol == 0:
        logger.info(f'The distance from Moscow Ring Road to {coordinate} is {save} km')

    return f'{save} km e os bol: {bol}'