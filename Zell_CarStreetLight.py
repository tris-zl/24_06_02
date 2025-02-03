class CarStreetLight(object):
    '''
    This class represents a car street light.
    
    Attributes:
    status (str): The status of the car street light.

    Methods:
    set_status(): Sets the status of the car street light.
    get_status(): Returns the status of the car street light.
    '''
    def __init__(self, status: str):
        str: self.status = status

    def set_status(self, status: str) -> None:
        '''
        Sets the status of the car street light.
        
        Args:
        status (str): The status of the car street light.
        
        Returns:
        None
        '''
        self.status = status
        
    
    def get_status(self) -> str:
        '''
        Returns the status of the car street light.
        
        Args:
        None
        
        Returns:
        str: The status of the car street light.
        '''
        return self.status
        
    