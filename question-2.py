"""
Problem #2 - Fuel Station Design
Design a fuel station for 3 types of vehicles - Diesel, Petrol, and Electric. There are a fixed number of spots for each type of vehicle at the fuel station.

Implement the FuelStation class:
FuelStation(int diesel, int petrol, int electric) creates a  FuelStation object. The number of spots for each type of fuel is defined by the values provided to the constructor.
bool fuel_vehicle(str fuel_type)looks up whether there is an open slot that can provide fuel_type. A vehicle can only be fueled in a slot space of its fuel_type. If there is no slot free, return false, else put the vehicle in that fuel slot and return true.
bool open_fuel_slot(str fuel_type)releases a fuel slot of fuel_type so that another vehicle can be fueled. If you try to open a fuel slot, when all slots of a fuel_type are empty, return false. Otherwise, return true.

Input & Output:
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
fuel_station.fuel_vehicle("diesel") -> true (1 slot now open)
fuel_station.fuel_vehicle("petrol") -> true (1 slot now open)
fuel_station.fuel_vehicle("diesel") -> true (0 slots now open)
fuel_station.fuel_vehicle("electric") -> true (0 slots now open)
fuel_station.fuel_vehicle("diesel") -> false (0 slots open)
fuel_station.open_fuel_slot("diesel") -> true (1 slot now open)
fuel_station.fuel_vehicle("diesel") -> true (0 slots now open)
fuel_station.open_fuel_slot("electric") -> true (1 slot now open)
fuel_station.open_fuel_slot("electric") -> false (only 1 slot available at fuel station)
"""


class FuelStation:

    def __init__(self, diesel = 0, petrol = 0, electric = 0):

        self.diesel = diesel
        self.petrol = petrol
        self.electric = electric

        self.parking = {
            "diesel": diesel,
            "petrol": petrol,
            "electric": electric
        }

    def fuel_vehicle(self, fuel_type):
        if self.parking[fuel_type] > 0:
            self.parking[fuel_type] -= 1
            return True
        return False        

    def open_fuel_slot(self, fuel_type):

        if self.parking[fuel_type] == getattr(self,fuel_type):
            return False
        else:
            self.parking[fuel_type] += 1
            return True

    
if __name__ == "__main__":

    fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.fuel_vehicle("petrol"))
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.fuel_vehicle("electric"))
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.open_fuel_slot("diesel"))
    print(fuel_station.fuel_vehicle("diesel"))
    print(fuel_station.open_fuel_slot("electric"))
    print(fuel_station.open_fuel_slot("electric"))