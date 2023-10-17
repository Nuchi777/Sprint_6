import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка заказа самоката через кнопку:')
    @pytest.mark.parametrize('button_name', ['order_button_roadmap', 'order_button_header'])
    def test_order_scooter(self, driver, button_name):
        main_page = MainPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        main_page.click_order_button(button_name)
        order_page = OrderPage(driver)
        order_page.fill_name_field()
        order_page.fill_surname_field()
        order_page.fill_address_field()
        order_page.fill_metro_station_field()
        order_page.fill_telephone_number_field()
        order_page.click_next_button()
        order_page.fill_delivery_data_field()
        order_page.fill_rent_period_field()
        order_page.fill_color_scooter_field()
        order_page.fill_comment_field()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.check_status_window_is_visible()





