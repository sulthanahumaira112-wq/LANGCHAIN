from langchain_core.tools import tool
from database import customers,orders

@tool
def get_customer(customer_id:int):
    """Find customer information using customer ID."""

    customer=customers.get(customer_id)

    if not customer:
        return "Customer not found."

    return customer

@tool
def get_order(order_id:int):
    """Find order information using order ID."""

    order = orders.get(order_id)

    if not order:
        return "Order not found."

    return order

@tool
def calculate_total(price: float, quantity: int):
    """Calculate total price of products."""

    return price * quantity


@tool
def get_order_status(order_id: int):
    """Check the delivery status of an order."""
    order = orders.get(order_id)

    if not order:
        return "Order not found."

    return order["status"]