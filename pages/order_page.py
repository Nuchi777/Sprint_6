import time
import re

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.locators import OrderPageLocators
import datetime
import random
from faker import Faker

faker = Faker('ru_RU')


class OrderPage(BasePage):
    locators = OrderPageLocators()

    def fill_all_fields_person(self):
        self.element_is_visible(self.locators.NAME).send_keys(faker.first_name())
        self.element_is_visible(self.locators.SURNAME).send_keys(faker.last_name())
        self.element_is_visible(self.locators.DELIVERY_ADDRESS).send_keys(f"{faker.street_title()}, {faker.building_number()}")
        self.element_is_visible(self.locators.METRO_STATION_LIST).send_keys(random.choice([' Новокосино', ' Бауманская', ' Таганская', ' Фили']))
        self.element_is_visible(self.locators.METRO_STATION).click()
        self.element_is_visible(self.locators.TEL_NUMBER).send_keys(f"+7{random.choice(['925', '916', '903', '965'])}{random.randint(1000000, 9999999)}")

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

    def click_next_button(self):
        self.find_element(self.locators.NEXT_BUTTON).click()

    def click_yes_button(self):
        self.element_is_visible(self.locators.YES_BUTTON).click()

    def check_status_window_is_visible(self):
        return self.element_is_visible(self.locators.STATUS_WINDOW)
