"""
Module represents restaurant working processes
"""
import logging
import random
import abc
import datetime
import sys




class Order:
    """
    Class realize order for restaurant

    Attributes
    ----------
    chosen_dishes: list
        list of chosen dishes by client
    ready_dishes: list
        list of ready dishes from kitchen
    address: str
        address of client or table number if client not distant
    is_ready: bool
        order state, True if ready, False fi not ready
    """

    def __init__(self, dishes: list, address: str):
        """Order constructor"""
        self.chosen_dishes = dishes
        self.address = address
        self.is_ready = False
        self.ready_dishes = []

    def __repr__(self):
        return f"chosen_dishes={self.chosen_dishes}, address={self.address}, " \
               f"isready={self.is_ready}, ready_dishes={self.ready_dishes}"




class Menu:
    """
    Class realize menu for restaurant

    Attributes
    ---------
    list_of_dishes: list
        dishes im menu
    out_of_service: list
        dishes that cant be cooked
    """

    def __init__(self, dishes: list):
        """Menu constructor"""
        self.list_of_dishes = dishes
        self.out_of_service = []


class Employee(abc.ABC):
    """
    Abstract class for employee person

    Methods
    -------
    raise_salary(amount: float): None
        raises person salary on given amount

    Attributes
    ----------
    name: str
        name of person
    d_o_b: datetime
        date of birth
    sex: str
        sex of person
    phone_number: str
        phone number of person
    salary: float
        salary of person
    """

    def __init__(self, name: str, d_o_b: datetime, sex: str, phone_number:str, salary: float):
        """
        Constructor
        :param name: str, name of person
        :param d_o_b: datetime, day of birth of person
        :param sex: str, sex of person
        :param phone_number: str
        :param salary: float salary of person
        :raise ValueException if salary les than zero or equal
        """
        self._name = name
        self._d_o_b = d_o_b
        self._sex = sex
        self._phone_number = phone_number
        self._salary = salary

    def __setattr__(self, key, value):
        """
        Checks for not negative salary value
        """
        if key == "salary" and value <= 0:
            raise ValueError( "Salary cant be negative or zero!")
        self.__dict__[key] = value

    def raise_salary(self, amount: float):
        """
        Raises salary
        :param amount: float
        :return: None
        """
        self._salary += amount

    def __str__(self):
        return f"{self._name}, {self._sex}, {self._d_o_b}, {self._salary}"


class ServiceMan(abc.ABC):
    """
    Abstract class for service personal

    Methods
    -------
    correct_order(str):
        correct order if some dishes of order is out of service
    show_menu(Menu): list
        returns list of string from menu list_of_dishes
    take_order(Order):
        correct and add order in list of orders

    Attributes
    ----------
    orders: list of taken orders
    ready_order: Order, ready order from kitchen
    menu: Menu, menu for clients
    """

    def __init__(self, menu: Menu):
        """Constructor for service man object"""
        self.orders = []
        self.ready_order = None
        self._menu = menu

    def correct_order(self, order: Order):
        """
        Removes dishes that out of service

        """
        for dish in order.chosen_dishes:
            if dish in self._menu.out_of_service:
                order.chosen_dishes.remove(dish)
        return order

    def take_order(self, order: Order):
        """Adds order in list of orders """
        if order.is_ready:
            self.ready_order = order
        else:
            self.orders.append(self.correct_order(order))


    def show_menu(self):
        """Shows menu to client as list"""
        return self._menu.list_of_dishes


    @abc.abstractmethod
    def send_to_kitchen(self):
        """Must be defines in child classes"""
        ...


class Customer(abc.ABC):
    """
    Abstract class for any sort of clients

    Methods
    -------
    create_order(list): Order
        method that creates order from list of dishes from menu
        abstract method, must be realized in child classes

    Attributes
    ----------
    name: str name of a client
    """

    def __init__(self, name):
        """Constructor for client, should called in child classes"""
        self.name = name

    @abc.abstractmethod
    def receive_order(self, order: Order):
        """Receives ready order from ServiceMan  """



class Kitchen:
    """
    Class realize restaurants kitchen

    Methods
    -------
    prepare_order(Order): Order
        prepare dishes form order set is_ready True and adds to ready_orders_list
    back_ready_order(): Order
        returns ready order
    take orders(list):
        takes orders from waiter
    edit menu(str, int):
        add or remove dish from menu

    Attributes
    ----------
    orders_in_work: list
    ready_orders: list
    """

    def __init__(self):
        self._orders_in_work = []
        self._ready_orders = []

    def prepare_order(self):
        """
        Method describes preparing order from
        orders_in_work list
        :return: None
        """
        order = self._orders_in_work.pop()
        for dish in order.chosen_dishes:
            order.ready_dishes.append(dish)
        order.chosen_dishes.clear()
        order.is_ready = True
        self._ready_orders.append(order)

    def take_orders(self, orders: list):
        """
        Takes orders from waiters
        and adds it to _orders_in_work list
        """
        self._orders_in_work += orders

    def back_ready_order(self):
        """
        Returns ready order from _ready_ready_dishes list
        :return: Order
        """
        return self._ready_orders.pop()

    @staticmethod
    def edit_menu(menu: Menu, dish, ind: int ):
        """
        Edit menu.
        ind==1 add dish to list_of_dishes
        ind==2 remove dish from list_of_dishes
        ind==3 add dish to out_of_service
        ind==4 remove dish to out_of_service

        :param menu: Menu
        :param dish: srt
        :param ind: int
        :return: None
        """
        if ind == 1 and dish not in menu.list_of_dishes:
            menu.list_of_dishes.append(dish)
        if ind == 2 and dish in menu.list_of_dishes:
            menu.list_of_dishes.remove(dish)
        if ind == 3 and dish not in menu.out_of_service:
            menu.out_of_service.append(dish)
        if id == 4 and dish in menu.out_of_service:
            menu.out_of_service.remove(dish)


class Waiter(Employee, ServiceMan):
    """
    Class realize waiter of restaurant

    Methods
    -------
    send_to_kitchen(): Order
        sends all Orders to kitchen
    serve_client(): Order
        returns ready order to client
    """
    def __init__(self,name: str, d_o_b: datetime, sex: str,
                 phone_number:str, salary: float, menu: Menu):
        """Waiter constructor"""
        Employee.__init__(self, name, d_o_b, sex, phone_number, salary )
        ServiceMan.__init__(self, menu)

    def send_to_kitchen(self):
        """Returns all orders"""
        temp = self.orders[:]
        self.orders.clear()
        return temp

    def serve_client(self):
        """Return ready dish"""
        temp = self.ready_order
        self.ready_order = None
        return temp


class Bartender(Employee, ServiceMan):
    """
    Class realize bartender for restaurant

    Methods
    ------
    _mix_drink(Order): Order
        prepares drink and add to ready order
    return_drink(Order): Order
        returns ready drink to client
    """

    def __init__(self,name: str, d_o_b: datetime, sex: str,
                 phone_number:str, salary: float, menu: Menu):
        """Bartender constructor"""
        Employee.__init__(self, name, d_o_b, sex, phone_number, salary )
        ServiceMan.__init__(self, menu)

    @staticmethod
    def _mix_drink(order: Order):
        for dish in order.chosen_dishes:
            order.ready_dishes.append(dish)
        order.chosen_dishes.clear()
        order.is_ready = True
        return order

    def return_to_client(self):
        """Mix order and return ready order"""
        order = self.orders.pop()
        return self._mix_drink(order)

    def send_to_kitchen(self):
        pass


class ClientManager(Employee, ServiceMan):
    """
    Class realize client manager  for delivery service
    Methods
    ------
    send_to_bar(): Order
        sends order to bar
    pack_order(Order): None
        packs order from kitchen and bar to one

    Attributes
        b_menu: Menu
        Menu of drinks


    """
    def __init__(self,name: str, d_o_b: datetime, sex: str,
                 phone_number:str, salary: float, menu: Menu, b_menu: Menu):
        """ClientManager constructor"""
        Employee.__init__(self, name, d_o_b, sex, phone_number, salary )
        ServiceMan.__init__(self, menu)
        self.b_menu = b_menu
        self.b_orders = []
        self.ready_bar_order = None

    def send_to_bar(self):
        """
        Sends order to bar
        :return: Order
        """
        return self.b_orders.pop()

    def take_bar_order(self, order: Order):
        """Takes bar order from client"""
        self.b_orders.append(self.correct_order(order))

    def take_from_bar(self, order: Order):
        """Takes order from bartender"""

        self.ready_bar_order = order

    def send_to_kitchen(self):
        """
        Send orders to kitchen
        :return: orders
        """
        temp = self.orders[:]
        self.orders.clear()
        return temp

    def pac_order(self):
        """Pack two orders in one"""
        tmp_order = self.ready_order
        tmp_bar_order = self.ready_bar_order
        self.ready_bar_order = None
        if not tmp_bar_order:
            return
        for dish in tmp_bar_order.ready_dishes:
            tmp_order.ready_dishes.append(dish)
        self.ready_order = tmp_order

    def return_to_courier(self):
        """Return order to courier"""
        tmp = self.ready_order
        self.ready_order = None
        return tmp

    def show_bar_menu(self):
        """Returns drinks from bar menu"""
        return self.b_menu.list_of_dishes


class Courier(Employee):
    """
    Class represents courier of delivery service
    Methods
    ------
    delivery_to_client(): Order
        delivers order to distant client

    Attributes
    ----------
    package: list
        list or ready orders
    """

    def __init__(self, name: str, d_o_b: datetime, sex: str, phone_number: str, salary: float):
        """Constructor courier class"""
        super().__init__(name, d_o_b, sex, phone_number, salary)
        self.package = []

    def delivery_to_client(self):
        """
        Returns package to client
        :return: Order
        """
        tmp = self.package.pop()
        return tmp

    def take_ready_order(self, order: Order):
        """Takes order from manager"""
        self.package.append(order)


class DeliveryService:
    """
    Class realize delivery service of restaurant

    Attributes
    ----------
    client_manager: ClientManager
    courier: Courier
    """

    def __init__(self, manager: ClientManager, courier: Courier):
        self.manager = manager
        self.courier = courier

    def __str__(self):
        ret_str = str(self.manager) + " "
        ret_str += str(self.courier)
        return ret_str



class Client(Customer):
    """
    Class describes guest of restaurant

    Methods
    -------
    create_order(list): Order
        Method creates Order menus dishes

    Attributes
    ----------
    table_number: int
        address of client
    dishes: Order
        order with is_ready True
    """

    def __init__(self, name: str, table_number: str):
        """Client constructor"""
        super().__init__(name)
        self.table_number = table_number
        self.dishes = None

    def create_order(self, dishes: list, number_of_dishes: int):
        """
        Creates order from menu and table number
        """
        order = [random.choice(dishes) for _ in range(number_of_dishes)]
        return Order(order, self.table_number)


    def receive_order(self, order: Order):
        """Receives ready order from ServiceMan  """
        self.dishes = order



class DistantClient(Customer):
    """
        Class describes distant client of restaurant

        Methods
        -------
        create_order(list): Order
            Method creates Order menus dishes

        Attributes
        ----------
        table_number: int
            address of client
        """

    def __init__(self, name: str, address: str):
        """Client constructor"""
        super().__init__(name)
        self.address = address
        self.dishes = None

    def create_order(self, dishes: list, number_of_dishes: int):
        """Create order for distant client"""
        order = [random.choice(dishes) for _ in range(number_of_dishes)]
        return Order(order, self.address)

    def receive_order(self, order: Order):
        """Receives ready order from ServiceMan  """
        self.dishes = order


#  Create and setup console logging
logger = logging.getLogger("restaurant")
c_handler = logging.StreamHandler(stream=sys.stdout)
c_formatter = logging.Formatter("%(name)s - %(message)s ")
c_handler.setFormatter(c_formatter)
c_handler.setLevel(logging.INFO)
logger.addHandler(c_handler)
logger.setLevel(logging.INFO)


positions = ["steak", "pasta", "souse"]
kitchen_menu = Menu(positions)
logger.info("Creates menu with %s", positions)
drinks = ["beer", "whiskey", "mojito", "pina colada"]
bar_menu = Menu(drinks)
logger.info("Creates menu for bar with %s", drinks)
waiter = Waiter("Bob", datetime.datetime(1990,2,10), "m", "+1002265", 7750, kitchen_menu)

bartender = Bartender("Joe", datetime.datetime(1991,12,13), "m", "+1003587",79000, bar_menu)

kitchen = Kitchen()

cl_manager = ClientManager("Lisa", datetime.datetime(2000, 8, 17),
                           "f", "+1005689", 8000, kitchen_menu, bar_menu)
d_courier = Courier("Jack", datetime.datetime(2005, 7, 30), "m", "+1007856", 6000)
d_service = DeliveryService(cl_manager, d_courier)


guest = Client("Tom", "5")
d_client = DistantClient("Sara", "Evergreen st, 1")
ordr = guest.create_order(waiter.show_menu(), 2)
logger.info("Guest creates order with: %s", ordr.__repr__())
waiter.take_order(ordr)
logger.info("Waiter takes order %s", ordr)
kitchen.take_orders(waiter.send_to_kitchen())
logger.info("Waiter send order %s to kitchen", ordr)
kitchen.prepare_order()
logger.info("Kitchen cooks...")
waiter.take_order(kitchen.back_ready_order())
logger.info("Kitchen returns ready order to waiter: %s", waiter.ready_order)
guest.receive_order(waiter.serve_client())
logger.info("Waiter serves client. It return %s", guest.dishes)
logger.info("Client %s decided go to bar and make some order", guest.name)
b_order = guest.create_order(bartender.show_menu(), 1)
logger.info("Guest make order %s", b_order)
bartender.take_order(b_order)
logger.info("Bartender takes order %s", bartender.orders)
guest.receive_order(bartender.return_to_client())
logger.info("Client receive drinks %s", guest.dishes)

logger.info(">>>>>>>Distant client situation")
#  Distant client situation
kitchen_menu = d_service.manager.show_menu()
bar_menu = d_service.manager.show_bar_menu()
k_order = d_client.create_order(kitchen_menu, 2)
logger.info("Distant client maks order from kitchen menu %s", k_order)
d_service.manager.take_order(k_order)
logger.info("Manager takes order %s", d_service.manager.orders)
b_order = d_client.create_order(bar_menu, 1)
logger.info("Distant client maks order from bar menu %s", b_order)
d_service.manager.take_bar_order(b_order)
logger.info("Manager takes  bar order %s", d_service.manager.b_orders)
kitchen.take_orders(d_service.manager.send_to_kitchen())
logger.info("Manager send order to kitchen")
kitchen.prepare_order()
logger.info("Kitchen cooks...")
d_service.manager.take_order(kitchen.back_ready_order())
logger.info("Kitchen returns ready order to waiter: %s",
            d_service.manager.ready_order)
b_order = d_service.manager.send_to_bar()
logger.info("Manager send order %s to bar", b_order)
bartender.take_order(b_order)
logger.info("Bartender takes order %s", bartender.orders)
ready_bar_order = bartender.return_to_client()
logger.info("Bartender returns order %s", ready_bar_order)
d_service.manager.take_from_bar(ready_bar_order)
logger.info("Manager  takes ready bar order %s", d_service.manager.ready_bar_order)
d_service.manager.pac_order()
logger.info("Manager  packs two orders together order %s", d_service.manager.ready_order)
d_service.courier.take_ready_order(d_service.manager.return_to_courier())
logger.info("Manager returns order to courier %s", d_service.courier.package)
d_client.receive_order(d_service.courier.delivery_to_client())
logger.info("Courier returns order to client %s\n"\
            " Client takes an order %s",
            d_service.courier.package, d_client.dishes)
