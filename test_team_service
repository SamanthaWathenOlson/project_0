from customer_exceptions.bad_customer_info import BadCustomerInfo
from data_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from objects.customer_class import CustomerId
from service_layer.customer_services.customer_service_interfaces import CustomerServiceInterface

class CustomerServiceImp(CustomerServiceInterface):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer.dao = customer.dao

    @abstractmethodcustomerId
    def service_create_team(self, customer_id: CustomerID) -> CustomerId:
        if type(customer_id.customer_name) != str:  #checking that the team name is a string
           raise BadCustomerInfo("Please put in valid customer name") #raise an exception
        elif type(customer.customer_id) != str: #checking home city
            raise BadCustomerInfo("Please put in valid customer id") #raise and exception
        for previous_customer in self.customer_dao.customer_list: ##loop through existing customer to vallidate business
            if previous_customer. customer_id ==customer_id.customer_name:
                raise BadCustomerInfo("This customer already exists in the database")
            elif previous_customer.address == customer_id.customer_address:
                raise BadCustomerInfo ("This customer id already exits in the database")
        return self.customer_dao.update_customer_by_id(customer_id)

    @abstractmethod
    def service_get_team_information_by_id(self, customer_id: CustomerId) -> CustomerId
        if type(customer_id) == int:
            return self.customer_dao.get_customer_information_by_id(customer_id)
        else:
            raise BadCustomerInfo("Please provide valid customer id"")

    @abstractmethod
    def update_customer_by_id(self, customer_id: CustomerId) -> CustomerId
        def service_create_team(self, customer_id: CustomerID) -> CustomerId
            if type(team.team) != str:  # checking that the team name is a string
                raise BadCustomerInfo("Please put in valid customer name")  # raise an exception
            #elif type(customer.address) 1= str:  # checking home city
            #    raise BadCustmerInfo("Please put in valid customer address")  # raise and exception
            for previous_customer in self.customer_dao.customer_list:  ##loop through existing customer to vallidate business
                if previous_customer.customer_id == customer.customer_name:
                    raise BadCustomerInfo("This customer already exists in the database")
            #    elif previous_customer.address == customer.customer_address:
            #       raise BadCustomerInfo("This city name already exits in the database")
            return self.customer_dao.update_customer_by_id(customer)


    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool
        if type(customer_id) == int:
            return self.customer_dao.delete_customer_by_id(customer_id)
        else:
            raise BadCustomerInto("please provide valid customer id")
