import pytest
from order import MenuItem, OrderItem, PricingConfig, FoodOrder

# Валідація

def test_menu_item_validation():
    with pytest.raises(ValueError):
        MenuItem(code="", name="Burger", price=10)
    with pytest.raises(ValueError):
        MenuItem(code="B1", name="", price=10)
    with pytest.raises(ValueError):
        MenuItem(code="B1", name="Burger", price=0)

def test_order_item_validation():
    item = MenuItem(code="B1", name="Burger", price=10)
    with pytest.raises(ValueError):
        OrderItem(menu_item=item, quantity=0)

def test_add_item_type():
    order = FoodOrder()
    with pytest.raises(TypeError):
        order.add_item("not an OrderItem")

# Операції з замовленням

def test_add_and_subtotal():
    order = FoodOrder()
    burger = MenuItem(code="B1", name="Burger", price=10)
    pizza = MenuItem(code="P1", name="Pizza", price=20)

    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(pizza, 1))

    assert order.subtotal() == 40

def test_merge_same_item():
    order = FoodOrder()
    burger = MenuItem(code="B1", name="Burger", price=10)
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(burger, 3))
    assert order.items[0].quantity == 5

def test_remove_item():
    order = FoodOrder()
    burger = MenuItem(code="B1", name="Burger", price=10)
    pizza = MenuItem(code="P1", name="Pizza", price=20)
    order.add_item(OrderItem(burger, 1))
    order.add_item(OrderItem(pizza, 1))

    order.remove_item("B1")
    assert order.subtotal() == 20

    with pytest.raises(ValueError):
        order.remove_item("NON_EXISTENT")

# Розрахунки

def test_service_fee():
    order = FoodOrder()
    item = MenuItem(code="B1", name="Burger", price=100)
    order.add_item(OrderItem(item))
    fee = order.service_fee_amount(order.subtotal())
    assert fee == 5.0

def test_total_with_promo():
    order = FoodOrder()
    item = MenuItem(code="B1", name="Burger", price=100)
    order.add_item(OrderItem(item))
    order.apply_promo("FOOD10")
    total = order.total()
    assert total == 94.5

# Промокоди

def test_invalid_promo():
    order = FoodOrder()
    item = MenuItem(code="B1", name="Burger", price=100)
    order.add_item(OrderItem(item))
    with pytest.raises(ValueError):
        order.apply_promo("INVALIDCODE")

def test_promo_over_100_percent():
    pricing = PricingConfig(promo_discounts={"BIG":150})
    order = FoodOrder(pricing)
    item = MenuItem(code="B1", name="Burger", price=100)
    order.add_item(OrderItem(item))
    with pytest.raises(ValueError, match="configured promo out of range 0..100"):
        order.apply_promo("BIG")

# Невалідна конфігурація

def test_service_fee_over_100_percent():
    pricing = PricingConfig(service_fee_percent=150)
    order = FoodOrder(pricing)
    item = MenuItem(code="B1", name="Burger", price=100)
    order.add_item(OrderItem(item))
    with pytest.raises(ValueError):
        order.service_fee_amount(order.subtotal())
