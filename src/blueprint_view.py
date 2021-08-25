from flask import Blueprint
# importing the functions to create a point and check it
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Feature
# importing the mkad polygon to check with the point
from mkad_polygon import polygon
# importing the numpy to create the calc_distance function
import numpy as np
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()
# importing from .env the API Token
API_TOKEN = os.getenv('API_TOKEN')

# configuring the log
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
logging.basicConfig(filename='distance.log',
                    filemode='a',
                    level=logging.INFO,
                    format=log_format)

logger = logging.getLogger('root')

# creating the blueprint
distance_bp = Blueprint('distance_bp', __name__)


def calc_distance(lat1, lat2, lon1, lon2):
    '''
    function to calculate the distance between mkad and the adress
    '''
    r = 6371
    dlat = np.deg2rad(lat2 - lat1)
    dlon = np.deg2rad(lon2 - lon1)
    a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.deg2rad(lat1)) * \
        np.cos(np.deg2rad(lat2)) * np.sin(dlon/2) * np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    d = r * c
    return round(d)


@distance_bp.route('/<adress>', methods=['GET'])
def distante(adress):
    '''
    the distance function where receive and check the request
    '''

    # creating 2 list, one to save the main coordinate of mkad
    # another to save the coordinate of adress
    list1 = [37.842762, 55.774558]
    list2 = []

    # boolean variable
    bol = 0

    # checking if the parameter is coordinate
    # or adress
    if ',' in adress:
        # if coordinate split the string on a list
        coord_list = adress.split(',')
        # then append the values on the list2
        list2.append(coord_list[0])
        list2.append(coord_list[1])
        # create a point to check on mkad polygon
        point = Feature(geometry=Point((float(list2[0]), float(list2[1]))))
        print(boolean_point_in_polygon(point, polygon))
        # if the point is inside polygon mkad then add 1 to bol variable
        if boolean_point_in_polygon(point, polygon) is True:
            bol += 1

    else:
        # if not a coordinate
        # search on the api
        r = requests.get(
            f'https://api.mapbox.com/geocoding/v5/mapbox.places/{adress}.json?access_token={API_TOKEN}')
        # get the response
        response = r.json()
        # append the coordinate of the adress on list2
        list2.append(response['features'][0]['center'][0])
        list2.append(response['features'][0]['center'][1])
        # create a point to check on mkad polygon
        point = Feature(geometry=Point((float(list2[0]), float(list2[1]))))
        print(boolean_point_in_polygon(point, polygon))
        # if the point is inside polygon mkad then add 1 to bol variable
        if boolean_point_in_polygon(point, polygon) is True:
            bol += 1

    # creating a variable with the result of the calc_distance function
    save = str((calc_distance(float(list1[1]), float(
        list2[0]), float(list1[0]), float(list2[1]))))

    # checking if the bol variable is equal to 0
    if bol == 0:
        # then add the result to the distance.log file
        # if the file not exists it will be created then add the result
        logger.info(
            f'The distance from Moscow Ring Road to {adress} is {save} km')

    return f'{save} km e os bol: {bol}'
