from Zell_CarStreetLight import CarStreetLight

class PedestrianStreetLight(CarStreetLight):
    '''
    This class represents a pedestrian street light.
    
    Attributes:
    status (str): The status of the pedestrian street light.
    
    Methods:
    set_status(): Sets the status of the pedestrian street light.
    get_status(): Returns the status of the pedestrian street light.
    '''
    def __init__(self, status: str):
        super(PedestrianStreetLight, self).__init__(status)
