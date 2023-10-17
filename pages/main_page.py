import time

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


    def check_accordian(self, accordian_num):
        accordian = {'0':
                         {'title': self.locators.ACCORDIAN_TITLE_0, 'content': self.locators.ACCORDIAN_CONTENT_0},
                     '1':
                         {'title': self.locators.ACCORDIAN_TITLE_1, 'content': self.locators.ACCORDIAN_CONTENT_1},
                     '2':
                         {'title': self.locators.ACCORDIAN_TITLE_2, 'content': self.locators.ACCORDIAN_CONTENT_2},
                     '3':
                         {'title': self.locators.ACCORDIAN_TITLE_3, 'content': self.locators.ACCORDIAN_CONTENT_3},
                     '4':
                         {'title': self.locators.ACCORDIAN_TITLE_4, 'content': self.locators.ACCORDIAN_CONTENT_4},
                     '5':
                         {'title': self.locators.ACCORDIAN_TITLE_5, 'content': self.locators.ACCORDIAN_CONTENT_5},
                     '6':
                         {'title': self.locators.ACCORDIAN_TITLE_6, 'content': self.locators.ACCORDIAN_CONTENT_6},
                     '7':
                         {'title': self.locators.ACCORDIAN_TITLE_7, 'content': self.locators.ACCORDIAN_CONTENT_7}}
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, section_content

    def click_accordian_title(self, title_locator):
        self.element_is_visible(title_locator).click()

    def check_accordian_content(self, content_locator):
        content_text = self.find_element(content_locator).text
        return content_text







