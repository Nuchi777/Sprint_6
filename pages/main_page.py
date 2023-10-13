from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_order_button_roadmap(self):
        self.element_is_visible(self.locators.ORDER_BUTTON_ROADMAP).click()

    def click_order_button_header(self):
        self.element_is_clickable(self.locators.ORDER_BUTTON_HEADER).click()

    def click_order_button(self, button_name):
        if button_name == 'order_button_roadmap':
            self.click_order_button_roadmap()
        elif button_name == 'order_button_header':
            self.click_order_button_header()

    def click_to_logo_scooter(self):
        self.element_is_visible(self.locators.LOGO_SCOOTER).click()

    def check_home_header_visible(self):
        return self.element_is_visible(self.locators.HOME_HEADER_MAIN_PAGE_SCOOTER).text


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
