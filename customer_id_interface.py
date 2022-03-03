from abc import ABC, abstractmethod
from objects.team_class_infromation import CustomerId

class CustomnerIdInterface(ABC):

    @abstractmethod
    def service_deposit(self, value, customer_id):
       pass

    @abstractmethod
    def service_withdraw(self, value, customer_id):
        pass

    @abstractmethod
    def service_transfer(self, value, customer_id):
        pass
