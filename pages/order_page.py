import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.locators import OrderPageLocators
import datetime
import random


class OrderPage(BasePage):
    locators = OrderPageLocators()

    def fill_all_fields_person(self):
        self.element_is_visible(self.locators.NAME).send_keys('Иван')
        self.element_is_visible(self.locators.SURNAME).send_keys('Иванов')
        self.element_is_visible(self.locators.DELIVERY_ADDRESS).send_keys('Балашиха, ул. Автозаводская, 5')
        self.element_is_visible(self.locators.METRO_STATION_LIST).click()
        self.element_is_visible(self.locators.METRO_STATION).click()
        self.element_is_visible(self.locators.TEL_NUMBER).send_keys('+7888888888')

    def click_next_button(self):
        self.find_element(self.locators.NEXT_BUTTON).click()

    def fill_all_fields_rent(self):
        date_today = str(datetime.date.today())
        date_tomorrow = str(int(date_today[-2:]) + 1)
        self.element_is_visible(self.locators.DELIVERY_DATE).send_keys(date_tomorrow)
        self.element_is_visible(self.locators.DELIVERY_DATE).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.RENT_PERIOD).click()
        self.element_is_visible(self.locators.RENT_PERIOD_SELECTED).click()
        self.element_is_visible(self.locators.CHECKBOX_COLOR_SCOOTER).click()
        self.element_is_visible(self.locators.COMMENT_FOR_COURIER).send_keys('Позвонить за час!')

    def click_order_button(self):
        self.find_element(self.locators.ORDER_BUTTON).click()

    def click_yes_button(self):
        self.element_is_visible(self.locators.YES_BUTTON).click()

    def check_status_window_is_visible(self):
        return self.element_is_visible(self.locators.STATUS_WINDOW)
