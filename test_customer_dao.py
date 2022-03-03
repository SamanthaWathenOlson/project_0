from custom_exceptions.id_not_found import IdNotFound
from data_access_layer.customer_dao.customer_dao_imp import CustomerDAOImp
from objects.customer_class_info import Customer

customer_dao = CustomerDAOImp()
test_customer = Customer(0,1,"Samantha","Wathen")

def test_create_customer_success():
    test_customer = Customer(0,1,"Samantha","Wathen")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0

def test_catch_non_unique_id():
    test_customer = Customer(1,1,"Bad","Id",0)
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 1

def test_get_customer_info_by_id_success():
    result = customer_dao.get_customer_by_id(1)
    assert result.customer_id == 1

def test_get_customer_info_by_string():
    try:
        customer_dao.get_customer_by_id(1)
        assert False
    except IdNotFound as e:
        assert str(e) == "Please insert numeric numbers! Please try again.."

def test_get_customer_info_by_address():
    try:
        customer_dao.get_customer_by_id(1)
        assert False
    except IdNotFound as e:
        assert str(e) == "Customer Id not retrievable by address. Please try again."

def test_get_customer_using_non_existant_id():
    try:
        customer_dao.get_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"

def test_delete_customer_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result

def test_delete_customer_with_non_existant_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given: please try again!"

def test_delete_customer_with_string():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e: "please insert numeric numbers. Please try again." \
                            ""
def test_delete_customer_with_address():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e: "Customer Id not retrievable by address. Please try again."

