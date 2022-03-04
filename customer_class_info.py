lass Customer:

    def __init__(self, customer_id: int, account_id: int, first_name: str, last_name: str, address: str):
        self.customer_id = customer_id
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


"""
What will our customer need to identify them?

customers have names
customer have address
customers have account ids
customer need a unique id 
"""
