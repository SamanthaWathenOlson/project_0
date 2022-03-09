from abc import ABC, abstractmethod
from objects.team_class_infromation import CustomerId

class BankServiceInterface(ABC):

    @abstractmethod
    def service_balance(self, value, account_id):
        pass

    @abstractmethod
    def service_deposit(self, value, account_id):
       pass

    @abstractmethod
    def service_withdraw(self, value, account_id):
        pass

    @abstractmethod
    def service_transfer(self, value, account_id):
        pass

    @abstractmethod
    def service_transfer_full_amount(self, value, account_id):
        pass

       # create
   @abstractmethod
   def service_create_customer(self, customer: Customer) -> Customer:
       pass

   # read
    @abstractmethod
   def service_get_customer_information_by_id(self, customer_id: str) -> Customer:
        pass

    # update
    @abstractmethod
   def service_update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    # delete
    @abstractmethod
   def service_delete_team_by_id(self, customer_id: int) -> bool:
        pass
