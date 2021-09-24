"""This module is practice in OOP basics"""

import abc
import datetime


class Engine:

    """
    Parent class for all engines in Transport class


    Attributes
    ----------
    type_of_engine : str
        sets type of engine diesel or gasoline
    volume :float
        sets volume of engine, cant be 0 or negative

    """

    def __init__(self, type_of_engine: str, volume: float):
        """Constructor that initialize class fields"""
        self.type_of_engine = type_of_engine
        self.volume = volume

    def __setattr__(self, key, value):
        if key == "volume" and value <= 0:
            raise Exception("Volume of engine must be positive number")
        self.__dict__[key] = value


class SpecialDevice:
    """
    Class realize special equipment for SpecialAuto class

    Methods
    -------
    dev_start():
        runs special device
    dev_stop():
        stops special device

    Attributes
    ----------
    dev_name : str
        name of special device
    """
    def __init__(self, dev_name):
        self.dev_name = dev_name

    def dev_start(self):
        print(f"Device: {self.dev_name} is working")

    def dev_stop(self):
        print(f"Devise: {self.dev_name} is stopped")


class Transport:

    _transport_count = []
    """
    Parent class for all types of cars

    Methods
    --------
    is_winter:
        checks current season, returns True if winter is now 
    get_transport_instances:
        returns list of Transport instances
    refuel(amount):
        Set fuel_tank_level attribute on amount value
    change_tiers(tiers_type):
        Change tiers_type from Summer to Winter and back
    run(miles):
        abstract method must de implemented in child classes

    """

    @abc.abstractmethod
    def run(self):
        """
        Runs car by the miles amount and reduce fuel_tank_level
        Must be realized in child classes

        """
    @classmethod
    def get_transport_count(cls) -> list:
        """
        Returns _transport_count list
        """
        t_c = cls._transport_count[:]
        return t_c

    @staticmethod
    def is_winter() -> bool:
        """
        Check current month. If its winter, returns True, else False
        """
        today = datetime.datetime.today().month
        if 11 <= today <= 3:
            return True
        else:
            return False

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int):
        self.name = name
        self.fuel_tank_vol = fuel_tank_vol
        self.wheels_count = wheels_count
        self.fuel_tank_level = fuel_tank_level
        self.tiers_type = "Summer"
        self._transport_count.append(self)

    def refuel(self, amount: int):
        """Adds amount to fuel_tank_level
        and checks for overfuel
        :param amount amount of fuel that adds to fuel_tank_level

        """
        if amount + self.fuel_tank_level > self.fuel_tank_vol:
            print("Too much fuel. Cant refuel")
            return
        self.fuel_tank_level += amount
        print(f"Fuel in the tank: {self.fuel_tank_level}")

    def change_tiers(self):
        """Change tiers type on Summer or Winter"""
        if self.tiers_type == "Winter":
            self.tiers_type = "Summer"
            print("Tiers changes to summer")
        if self.tiers_type == "Summer":
            self.tiers_type = "Winter"
            print("Tiers changes to winter")


class Car(Transport, Engine):
    """
    Class describes car for personal use

    """
    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, engine_type: str, engine_volume: int, body_type: str):
        Transport.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level)
        Engine.__init__(self, engine_type, engine_volume)
        self.body_type = body_type

    def run(self):
        """Runs car on the amount of miles"""
        print(f"{self.name} runs")

    @property
    def show_info(self):
        return f"Name: {self.name}, fuel tank volume: {self.fuel_tank_vol}, wheel count: {self.wheels_count}" \
                f" fuel tank level: {self.fuel_tank_level}, engine type: {self.type_of_engine}," \
                f" engine volume: {self.volume}, body type: {self.body_type}, wheel type: {self.tiers_type}"


class Bus(Transport, Engine):

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, engine_type: str, engine_volume: float,
                 seats_amount: int):
        Transport.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level)
        Engine.__init__(self, engine_type, engine_volume)
        self.seats_amount = seats_amount

    def run(self):
        print(f"Bus {self.name} runs")

    @property
    def show_info(self):
        return f"Name: {self.name}, fuel tank volume: {self.fuel_tank_vol}, wheel count: {self.wheels_count}" \
                f" fuel tank level: {self.fuel_tank_level}, engine type: {self.type_of_engine}," \
                f" engine volume: {self.volume}, count of seats: {self.seats_amount}, wheel type: {self.tiers_type}"


class SpecialAuto(Transport, Engine, SpecialDevice):
    """
    Class realize some special auto (Concrete mixer for exmpl)
    """

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, engine_type: str, engine_volume: int, dev_name: str):
        Transport.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level)
        Engine.__init__(self, engine_type, engine_volume)
        SpecialDevice.__init__(self, dev_name)

    def run(self):
        print(f"Special auto: {self.name} runs")

    @property
    def show_info(self):
        return f"Name: {self.name}, fuel tank volume: {self.fuel_tank_vol}, wheel count: {self.wheels_count}" \
                f" fuel tank level: {self.fuel_tank_level}, engine type: {self.type_of_engine}," \
                f" engine volume: {self.volume}, device name: {self.dev_name}, wheel type: {self.tiers_type}"


car = Car("My car", 40, 4, 40, "gasoline", 4, "sedan")
print(car.show_info)
car.run()
bus = Bus("Double decker", 100, 6, 100, "diesel", 5, 40)
print(bus.show_info)
bus.run()
bus.change_tiers()
print(bus.show_info)
if Transport.is_winter():
    print("Time to change tiers type to Winter")
else:
    print("Time to change tiers type to Summer")

special_auto = SpecialAuto("Mixer Truck", 150, 6, 150, "Diesel", 6, "Concrete Mixer")
special_auto.dev_start()
special_auto.dev_stop()
print(special_auto.show_info)


