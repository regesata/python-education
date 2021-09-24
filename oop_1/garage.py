"""This module is practice in OOP basics"""

import abc
import datetime


class Engine:
    """
    Parent abstract class for all engines.

    Attributes
    ----------
    type_of_engine : str
        sets type of engine diesel or gasoline
    power :float
        sets power of engine, cant be 0 or negative

    Methods
    -------
    start_engine():
        starts motor - prints message that engine starts
    stop_engine():
        stops motor - prints message that engine stops

    """

    def __init__(self, type_of_engine: str, power: float):
        """Constructor that initialize class fields"""
        self.type_of_engine = type_of_engine
        self.power = power

    def __setattr__(self, key, value):
        """This method checks 'power' attribute, no prevent its value
         set in zero or less"""
        if key == "power" and value <= 0:
            raise Exception("Power of engine must be positive number")
        self.__dict__[key] = value

    @abc.abstractmethod
    def start_engine(self):
        pass

    @abc.abstractmethod
    def stop_engine(self):
        pass


class ICombustionEngine(Engine):
    """Class describes all inner combustion engines"""

    def __init__(self, type_of_engine: str, power: int, cylinders_count: int):
        Engine.__init__(self, type_of_engine, power)
        self.cylinders_count = cylinders_count

    def start_engine(self):
        print(f"Combustion {self.type_of_engine} motor started")

    def stop_engine(self):
        print(f"{self.type_of_engine} stopped")


class ElectricMotor(Engine):
    """Class describes all types of electric motors"""

    def __init__(self, type_of_engine: str, power: int):
        super().__init__(type_of_engine, power)

    def start_engine(self):
        """Starts electric motor"""

        print(f"{self.type_of_engine} electric motor started")

    def stop_engine(self):
        """Stops electric motor"""

        print(f"{self.type_of_engine} electric motor stopped")


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


class FlyingTransport(abc.ABC):
    """
    Class provides ability to fly for transport
    Methods
    -------
    run():
        run in the air

    """
    def run(self):
        print(f"{self.name} is flying")


class Airplane(FlyingTransport, Transport, ICombustionEngine):
    """Class describes airplane"""

    def __init__(self, name: str, fuel_tank: int, wheels_count: int, fuel_tank_level: int,
                 type_engine: str, power: int, cylinders_count: int):
        Transport.__init__(self, name, fuel_tank, wheels_count, fuel_tank_level)
        ICombustionEngine.__init__(self, type_engine, power, cylinders_count)
        FlyingTransport.__init__(self)

    def run(self):
        FlyingTransport.run(self)


class Car(Transport, ICombustionEngine):
    """
    Class describes car for personal use with inner combustion motor

    """

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, engine_type: str, engine_power: int, body_type: str,
                 engine_cylinder_count: int):
        Transport.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level)
        self.engine = ICombustionEngine.__init__(self, engine_type, engine_power, engine_cylinder_count)
        self.body_type = body_type

    def run(self):
        """Runs car"""
        print(f"{self.name} runs")

    @property
    def show_info(self):
        return f"Name: {self.name}, fuel tank volume: {self.fuel_tank_vol}, wheel count: {self.wheels_count}" \
               f" fuel tank level: {self.fuel_tank_level}, engine type: {self.type_of_engine}," \
               f" engine power: {self.power}, cylinders: {self.cylinders_count}," \
               f" body type: {self.body_type}, wheel type: {self.tiers_type}"


class Bus(Transport, ElectricMotor):
    """Class describes bus with electric motor"""

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, engine_type: str, power: float,
                 seats_amount: int):
        Transport.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level)
        self.engine = ElectricMotor.__init__(self, engine_type, power)
        self.seats_amount = seats_amount

    def run(self):
        print(f"Bus {self.name} runs")

    @property
    def show_info(self):
        return f"Name: {self.name}, battery capacity: {self.fuel_tank_vol}, wheel count: {self.wheels_count}" \
               f" charge level: {self.fuel_tank_level}, engine type: {self.type_of_engine}," \
               f" engine power: {self.power}, count of seats: {self.seats_amount}, wheel type: {self.tiers_type}"


class SpecialAuto(Transport, ICombustionEngine, SpecialDevice):
    """
    Class realize some special auto with hybrid motor (Concrete mixer for exmpl)
    """

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, ic_engine_type: str, ic_engine_power: int, ic_cylinders_count: int,
                 dev_name: str):
        Transport.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level)
        ICombustionEngine.__init__(self, ic_engine_type, ic_engine_power, ic_cylinders_count)

        SpecialDevice.__init__(self, dev_name)

    def run(self):
        print(f"Special auto: {self.name} runs")

    @property
    def show_info(self):
        return f"Name: {self.name}, fuel tank volume: {self.fuel_tank_vol}, wheel count: {self.wheels_count}" \
               f" fuel tank level: {self.fuel_tank_level}, " \
               f"combustion engine type: {self.type_of_engine}," \
               f" combustion engine power: {self.power}, cylinders: {self.cylinders_count} \n " \
               f" device name: {self.dev_name}, wheel type: {self.tiers_type}"


class FlyingCar(FlyingTransport, Car):
    """
    Class describes flying car
    Here we have diamond problem with methods run in Car class and FlyingTransport
    """

    def __init__(self, name: str, fuel_tank_vol: int, wheels_count: int,
                 fuel_tank_level: int, engine_type: str, engine_power: int, body_type: str,
                 engine_cylinder_count: int):
        Car.__init__(self, name, fuel_tank_vol, wheels_count, fuel_tank_level, engine_type, engine_power,
                     body_type, engine_cylinder_count)
        FlyingTransport.__init__(self)

    def run(self):
        FlyingTransport.run(self)
        Car.run(self)


# car = Car("My car", 40, 4, 40, "Diesel", 150, "Sedan", 4)
# print(car.show_info)
# car.run()
# bus = Bus("Double decker", 100, 6, 100, "Induction", 150, 40)
# print(bus.show_info)
# bus.run()
# bus.start_engine()
# bus.change_tiers()
# print(bus.show_info)
# if Transport.is_winter():
#     print("Time to change tiers type to Winter")
# else:
#     print("Time to change tiers type to Summer")
#
# special_auto = SpecialAuto("Mixer", 100, 6, 100, "Diesel", 150, 6, "Concrete mixer")
# special_auto.dev_start()
# special_auto.dev_stop()
# print(special_auto.show_info)
# special_auto.start_engine()

jet = Airplane("HellCat", 2000, 3, 2000, "Gasoline", 2000, 18)
jet.run()

nitra = FlyingCar("Nitra", 200, 4, 200, "gasoline", 200, "coupe", 6)
nitra.run()

