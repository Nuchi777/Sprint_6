import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step('Клик по кнопке "Заказать" внизу страницы')
    def click_order_button_roadmap(self):
        self.element_is_visible(self.locators.ORDER_BUTTON_ROADMAP).click()

    @allure.step('Клик по кнопке "Заказать" вверху страницы')
    def click_order_button_header(self):
        self.element_is_clickable(self.locators.ORDER_BUTTON_HEADER).click()

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self, button_name):
        if button_name == 'order_button_roadmap':
            self.click_order_button_roadmap()
        elif button_name == 'order_button_header':
            self.click_order_button_header()

    @allure.step('Клик по логотипу "Самокат"')
    def click_on_logo_scooter(self):
        self.element_is_visible(self.locators.LOGO_SCOOTER).click()

    @allure.step('Клик по логотипу "Яндекс"')
    def click_on_logo_yandex(self):
        self.element_is_visible(self.locators.LOGO_YANDEX).click()

    @allure.step('Проверка, что открылась главная страница "ЯндексСамокат"')
    def check_home_page_scooter_visible(self):
        return self.element_is_visible(self.locators.HOME_HEADER_MAIN_PAGE_SCOOTER).text

    @allure.step('Проверка, что открылась главная страница "Дзен"')
    def check_home_page_yandex_visible(self, index_page):
        self.switch_to_window(index_page)
        self.element_is_present(self.locators.BUTTON_SEARCH_MAIN_PAGE_DZEN)
        return self.get_current_url()

    def click_accordian_title(self, title_locator):
        self.element_is_visible(title_locator).click()

    def check_accordian_content(self, content_locator):
        content_text = self.find_element(content_locator).text
        return content_text







