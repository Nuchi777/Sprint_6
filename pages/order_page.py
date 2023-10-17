import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.locators import OrderPageLocators
import random
from faker import Faker

faker = Faker('ru_RU')


class OrderPage(BasePage):
    locators = OrderPageLocators()

    @allure.step('Заполнили поле "Имя" формы "Для кого самокат"')
    def fill_name_field(self):
        self.element_is_visible(self.locators.NAME).send_keys(faker.first_name())

    @allure.step('Заполнили поле "Фамилия" формы "Для кого самокат"')
    def fill_surname_field(self):
        self.element_is_visible(self.locators.SURNAME).send_keys(faker.last_name())

    @allure.step('Заполнили поле "Адрес" формы "Для кого самокат"')
    def fill_address_field(self):
        self.element_is_visible(self.locators.DELIVERY_ADDRESS).send_keys("г. Москва, ул. Ленина, д. 18")

    @allure.step('Выбрали станцию метро')
    def fill_metro_station_field(self):
        self.element_is_visible(self.locators.METRO_STATION_LIST).send_keys(
            random.choice(['А', 'Б', 'В', 'Г', 'Д', 'Е', 'С', 'П']))
        self.element_is_visible(self.locators.METRO_STATION).click()

    @allure.step('Заполнили поле "Телефон" формы "Для кого самокат"')
    def fill_telephone_number_field(self):
        self.element_is_visible(self.locators.TEL_NUMBER).send_keys(
            f"+7{random.choice(['925', '916', '903', '965'])}{random.randint(1000000, 9999999)}")

    @allure.step('Заполнили поле "Дата доставки" формы "Про аренду"')
    def fill_delivery_data_field(self):
        self.element_is_visible(self.locators.DELIVERY_DATE).send_keys(
            f"{faker.date_this_month(before_today=False, after_today=True)}")
        self.element_is_visible(self.locators.DELIVERY_DATE).send_keys(Keys.RETURN)

    @allure.step('Заполнили поле "Срок аренды" формы "Про аренду"')
    def fill_rent_period_field(self):
        self.element_is_visible(self.locators.RENT_PERIOD).click()
        self.element_is_visible(random.choice(self.locators.RENT_PERIOD_LIST)).click()

    @allure.step('Заполнили поле "Цвет самоката" формы "Про аренду"')
    def fill_color_scooter_field(self):
        self.element_is_visible(random.choice(self.locators.CHECKBOX_COLOR_SCOOTER_LIST)).click()
        self.element_is_visible(self.locators.COMMENT_FOR_COURIER).send_keys('Позвонить за час!')

    @allure.step('Заполнили поле "Комментарий курьеру" формы "Про аренду"')
    def fill_comment_field(self):
        self.element_is_visible(self.locators.COMMENT_FOR_COURIER).send_keys('Позвонить за час!')

    @allure.step('Клик по кнопке "Заказать" внизу формы')
    def click_order_button(self):
        self.find_element(self.locators.ORDER_BUTTON).click()

    @allure.step('Клик по кнопке "Далее" внизу формы')
    def click_next_button(self):
        self.find_element(self.locators.NEXT_BUTTON).click()

    @allure.step('Клик по кнопке "Да" во всплывающем окне')
    def click_yes_button(self):
        self.element_is_visible(self.locators.YES_BUTTON).click()

    @allure.step('Проверка, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_status_window_is_visible(self):
        return self.element_is_visible(self.locators.STATUS_WINDOW)
