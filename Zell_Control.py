from Zell_CarStreetLight import CarStreetLight
from Zell_PedestrianStreetLight import PedestrianStreetLight
import time

class Control(object):
    '''
    This class represents a control system for a car and pedestrian street light.
    
    Attributes:
    car_street_light (CarStreetLight): The car street light.
    pedestrian_street_light (PedestrianStreetLight): The pedestrian street light.
    
    Methods:
    main(): The main method that controls the car and pedestrian street light.
    '''
    def __init__(self):
        self.car_street_light = CarStreetLight("green")
        self.pedestrian_street_light = PedestrianStreetLight("red")

    def main(self) -> None:
        '''
        The main method that controls the car and pedestrian street light.
        
        Args:
        None
        
        Returns:
        None
        '''
        while True:
            push = input("Enter 'push' to cross the street or input 'exit' to not cross the street: ").strip().lower()
            if push == "push":
                # Car street light to red
                self.car_street_light.set_status("yellow")
                print(f'The car street light is {self.car_street_light.get_status()}')
                time.sleep(2)
                self.car_street_light.set_status("red")
                print(f'The car street light is {self.car_street_light.get_status()}')

                # The pedestrian street
                self.pedestrian_street_light.set_status("green")
                print(f'The pedestrian street light is {self.pedestrian_street_light.get_status()}')
                time.sleep(5)
                self.pedestrian_street_light.set_status("red")
                print(f'The pedestrian street light is {self.pedestrian_street_light.get_status()}')
                time.sleep(1)

                # Car street light to green
                self.car_street_light.set_status("yellow")
                print(f'The car street light is {self.car_street_light.get_status()}')
                time.sleep(1)
                self.car_street_light.set_status("green")
                print(f'The car street light is {self.car_street_light.get_status()}')
            elif push == "exit":
                break
            else:
                print("Invalid input.")
                continue
        

if __name__ == '__main__':
    control = Control()
    control.main()