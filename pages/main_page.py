from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()


    def click_to_accordion_heading_0(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_0)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_0).click()

    def click_to_accordion_heading_1(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_1).click()

    def click_to_accordion_heading_2(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_2)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_2).click()

    def click_to_accordion_heading_3(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_3)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_3).click()

    def click_to_accordion_heading_4(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_4)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_4).click()

    def click_to_accordion_heading_5(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_5)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_5).click()

    def click_to_accordion_heading_6(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_6)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_6).click()

    def click_to_accordion_heading_7(self):
        element = self.driver.find_element(*self.locators.ACCORDION_HEADING_7)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.element_is_clickable(self.locators.ACCORDION_HEADING_7).click()

    def get_accordion_panel_text_0(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_0).text

    def get_accordion_panel_text_1(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_1).text

    def get_accordion_panel_text_2(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_2).text

    def get_accordion_panel_text_3(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_3).text

    def get_accordion_panel_text_4(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_4).text

    def get_accordion_panel_text_5(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_5).text

    def get_accordion_panel_text_6(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_6).text

    def get_accordion_panel_text_7(self):
        return self.element_is_visible(self.locators.ACCORDION_PANEL_7).text

    def click_order_button_roadmap(self):
        self.element_is_visible(self.locators.ORDER_BUTTON_ROADMAP).click()

    def click_order_button_header(self):
        self.element_is_clickable(self.locators.ORDER_BUTTON_HEADER).click()

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
        return [section_title.text, section_content]
