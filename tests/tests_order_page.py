import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.mark.parametrize('button_name', ['order_button_roadmap', 'order_button_header'])
    def test_order_scooter(self, driver, button_name):
        # создали объект класса главной страницы
        main_page = MainPage(driver)
        # открыли тестовую страницу
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        # кликнули по кнопке "Заказать"
        main_page.click_order_button(button_name)
        # создали объект класса страницы оформления заказа "Для кого самокат"
        order_page = OrderPage(driver)
        # заполнили все элементы формы "Для кого самокат"
        order_page.fill_all_fields_person()
        # кликнули по кнопке "Далее" внизу формы
        order_page.click_next_button()
        # заполнили все элементы формы "Про аренду"
        order_page.fill_all_fields_rent()
        # кликнули по кнопке "Заказать" внизу формы
        order_page.click_order_button()
        # кликнули по кнопке "Да" всплывающего окна
        order_page.click_yes_button()
        # проверяем, что всплывающее окно "Заказ оформлен" появилось
        assert order_page.check_status_window_is_visible()





