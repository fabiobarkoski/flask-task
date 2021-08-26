from src.blueprint_view import calc_distance

class TestBlueprint:
    '''
    Test the blueprint functions
    '''

    def test_calc_distance(self):
        '''
        Test the calc_distance funtion with the following coordinates:
        37.842762, 55.774558 of the MKAD km 1;
        51.507351, -0.127696 of the London.
        The response will be 2514 or the function has errors
        '''
        assert calc_distance(55.774558, 51.507351, 37.842762, -0.127696) == 2514