from src.mkad_polygon import polygon
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Feature

class TestPolygon:
    '''
    Test the MKAD Polygon through of two different points,
    one inside the MKAD and another outside
    '''

    def test_one(self):
        '''
        Testing with Maryina Roshcha coordinate
        '''
        point1 = Feature(geometry=Point((55.795069, 37.616485)))
        assert boolean_point_in_polygon(point1, polygon) is True

    def test_two(self):
        '''
        Testing with London coordinate
        '''
        point2 = Feature(geometry=Point((51.507351, -0.127696)))
        assert boolean_point_in_polygon(point2, polygon) is False