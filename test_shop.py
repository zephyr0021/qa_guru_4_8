"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("apple", 200, "This is an apple", 500)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) == True
        assert product.check_quantity(1200) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:

    def test_add_product_in_cart(self, cart, product):
        cart.add_product(product)
        assert cart.products[product] == 1
        cart.add_product(product, 3)
        assert cart.products[product] == 4

    def test_remove_product_in_cart(self, cart, product):
        # проверка quantity не передан
        cart.add_product(product, 3)
        cart.remove_product(product)
        assert len(cart.products) == 0

        # проверка quantity = количество продуктов в позиции
        cart.add_product(product, 4)
        cart.remove_product(product, 4)
        assert len(cart.products) == 0

        # проверка quantity > количество продуктов в позиции
        cart.add_product(product, 2)
        cart.remove_product(product, 3)
        assert len(cart.products) == 0

        # проверка quantity < количество продуктов в позиции
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products[product] == 3

    def test_clear(self, cart, product, product2):
        cart.add_product(product, 5)
        cart.add_product(product2, 10)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price_in_cart(self, cart, product, product2):
        cart.add_product(product, 5)
        cart.add_product(product2, 10)
        assert cart.get_total_price() == 2500

    def test_buy_in_cart(self, cart, product, product2):
        # товаров не хватает на складе
        cart.add_product(product, 10001)
        cart.add_product(product2, 501)
        with pytest.raises(ValueError):
            cart.buy()
        cart.clear()

        # все товары на складе выкуплены
        cart.add_product(product, 1000)
        cart.add_product(product2, 500)
        cart.buy()
        assert product2.quantity == 0


    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
