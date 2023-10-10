from pages.main_page import MainPage


class TestMainPage:

    # Сколько это стоит? И как оплатить?
    def test_accordion_button_0(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_0()
        assert main_page.get_accordion_panel_text_0() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    # Хочу сразу несколько самокатов! Так можно?
    def test_accordion_button_1(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_1()
        assert main_page.get_accordion_panel_text_1() == 'Пока что у нас так: один заказ — один самокат. Если ' \
                                                         'хотите покататься с друзьями, можете просто сделать ' \
                                                         'несколько заказов — один за другим.'

    # Как рассчитывается время аренды?
    def test_accordion_button_2(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_2()
        assert main_page.get_accordion_panel_text_2() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим ' \
                                                         'самокат 8 мая в течение дня. Отсчёт времени аренды начинается с ' \
                                                         'момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                                                         'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    # Можно ли заказать самокат прямо на сегодня?
    def test_accordion_button_3(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_3()
        assert main_page.get_accordion_panel_text_3() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    # Можно ли продлить заказ или вернуть самокат раньше?
    def test_accordion_button_4(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_4()
        assert main_page.get_accordion_panel_text_4() == 'Пока что нет! Но если что-то срочное — всегда можно ' \
                                                         'позвонить в поддержку по красивому номеру 1010.'

    # Вы привозите зарядку вместе с самокатом?
    def test_accordion_button_5(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_5()
        assert main_page.get_accordion_panel_text_5() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает' \
                                                         ' на восемь суток — даже если будете кататься без передышек' \
                                                         ' и во сне. Зарядка не понадобится.'

    # Можно ли отменить заказ?
    def test_accordion_button_6(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_6()
        assert main_page.get_accordion_panel_text_6() == 'Да, пока самокат не привезли. Штрафа не будет, ' \
                                                         'объяснительной записки тоже не попросим. Все же свои.' \
 \
            # Я жизу за МКАДом, привезёте?

    def test_accordion_button_7(self, driver):
        main_page = MainPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        main_page.open()
        main_page.click_to_accordion_heading_7()
        assert main_page.get_accordion_panel_text_7() == 'Да, обязательно. Всем самокатов! И Москве, ' \
                                                         'и Московской области.'
