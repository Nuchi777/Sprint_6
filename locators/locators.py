from selenium.webdriver.common.by import By


class MainPageLocators:
    # Сколько это стоит? И как оплатить?
    ACCORDION_HEADING_0 = (By.ID, "accordion__heading-0")
    ACCORDION_PANEL_0 = (By.ID, "accordion__panel-0")
    # Хочу сразу несколько самокатов! Так можно?
    ACCORDION_HEADING_1 = (By.ID, "accordion__heading-1")
    ACCORDION_PANEL_1 = (By.ID, "accordion__panel-1")
    # Как рассчитывается время аренды?
    ACCORDION_HEADING_2 = (By.ID, "accordion__heading-2")
    ACCORDION_PANEL_2 = (By.ID, "accordion__panel-2")
    # Можно ли заказать самокат прямо на сегодня?
    ACCORDION_HEADING_3 = (By.ID, "accordion__heading-3")
    ACCORDION_PANEL_3 = (By.ID, "accordion__panel-3")
    # Можно ли продлить заказ или вернуть самокат раньше?
    ACCORDION_HEADING_4 = (By.ID, "accordion__heading-4")
    ACCORDION_PANEL_4 = (By.ID, "accordion__panel-4")
    # Вы привозите зарядку вместе с самокатом?
    ACCORDION_HEADING_5 = (By.ID, "accordion__heading-5")
    ACCORDION_PANEL_5 = (By.ID, "accordion__panel-5")
    # Можно ли отменить заказ?
    ACCORDION_HEADING_6 = (By.ID, "accordion__heading-6")
    ACCORDION_PANEL_6 = (By.ID, "accordion__panel-6")
    # Я живу за МКАДом, привезёте?
    ACCORDION_HEADING_7 = (By.ID, "accordion__heading-7")
    ACCORDION_PANEL_7 = (By.ID, "accordion__panel-7")

    # Кнопка "Заказать" в роадмапе
    ORDER_BUTTON_ROADMAP = (By.XPATH, "//button[contains(@class, 'UltraBig')]")
    # Кнопка "Заказать" в шапке
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")


class OrderPageLocators:
    # Для кого самокат
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    DELIVERY_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_LIST = (By.CSS_SELECTOR, "input[class='select-search__input']")
    METRO_STATION = (By.XPATH, ".//div[@class = 'select-search__select']")
    TEL_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # Про аренду
    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.XPATH, "//div[@class='Dropdown-control']")
    RENT_PERIOD_LIST = [(By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"),
                        (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"),
                        (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"),
                        (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']"),
                        (By.XPATH, "//div[@class='Dropdown-option' and text()='пятеро суток']"),
                        (By.XPATH, "//div[@class='Dropdown-option' and text()='шестеро суток']"),
                        (By.XPATH, "//div[@class='Dropdown-option' and text()='семеро суток']")]
    CHECKBOX_COLOR_SCOOTER_LIST = [(By.CSS_SELECTOR, "input[id='black']"), (By.CSS_SELECTOR, "input[id='grey']")]
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # окно "Хотите оформить заказ"
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")

    # окно "Заказ оформлен"
    STATUS_WINDOW = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']")
