from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.locators import OrderPageLocators
import random
from faker import Faker

faker = Faker('ru_RU')


class OrderPage(BasePage):
    locators = OrderPageLocators()

    def fill_all_fields_person(self):
        self.element_is_visible(self.locators.NAME).send_keys(faker.first_name())
        self.element_is_visible(self.locators.SURNAME).send_keys(faker.last_name())
        self.element_is_visible(self.locators.DELIVERY_ADDRESS).send_keys("г. Москва, ул. Ленина, д. 18")
        self.element_is_visible(self.locators.METRO_STATION_LIST).send_keys(random.choice(['А', 'Б', 'В', 'Г', 'Д', 'Е', 'С', 'П']))
        self.element_is_visible(self.locators.METRO_STATION).click()
        self.element_is_visible(self.locators.TEL_NUMBER).send_keys(f"+7{random.choice(['925', '916', '903', '965'])}{random.randint(1000000, 9999999)}")

    def fill_all_fields_rent(self):
        self.element_is_visible(self.locators.DELIVERY_DATE).send_keys(f"{faker.date_this_month(before_today=False, after_today=True)}")
        self.element_is_visible(self.locators.DELIVERY_DATE).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.RENT_PERIOD).click()
        self.element_is_visible(random.choice(self.locators.RENT_PERIOD_LIST)).click()
        self.element_is_visible(random.choice(self.locators.CHECKBOX_COLOR_SCOOTER_LIST)).click()
        self.element_is_visible(self.locators.COMMENT_FOR_COURIER).send_keys('Позвонить за час!')

    def click_order_button(self):
        self.find_element(self.locators.ORDER_BUTTON).click()

    def click_next_button(self):
        self.find_element(self.locators.NEXT_BUTTON).click()

    def click_yes_button(self):
        self.element_is_visible(self.locators.YES_BUTTON).click()

    def check_status_window_is_visible(self):
        return self.element_is_visible(self.locators.STATUS_WINDOW)
