from pages.main_page import MainPage
import allure


class TestMainPage:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    def test_accordian(self, driver):
        # создали объект класса главной страницы
        main_page = MainPage(driver)
        # открыли тестовую страницу
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        # кликнули по "title_0" текст заголовка "title" и описание "content" сохранили в переменные
        title_0, content_0 = main_page.check_accordian('0')
        # кликнули по "title_1" текст заголовка "title" и описание "content" сохранили в переменные
        title_1, content_1 = main_page.check_accordian('1')
        # кликнули по "title_2" текст заголовка "title" и описание "content" сохранили в переменные
        title_2, content_2 = main_page.check_accordian('2')
        # кликнули по "title_3" текст заголовка "title" и описание "content" сохранили в переменные
        title_3, content_3 = main_page.check_accordian('3')
        # кликнули по "title_4" текст заголовка "title" и описание "content" сохранили в переменные
        title_4, content_4 = main_page.check_accordian('4')
        # кликнули по "title_5" текст заголовка "title" и описание "content" сохранили в переменные
        title_5, content_5 = main_page.check_accordian('5')
        # кликнули по "title_6" текст заголовка "title" и описание "content" сохранили в переменные
        title_6, content_6 = main_page.check_accordian('6')
        # кликнули по "title_7" текст заголовка "title" и описание "content" сохранили в переменные
        title_7, content_7 = main_page.check_accordian('7')
        # Проверили, что текст "title" и описание "content" соответствуют текстам на сайте:
        assert title_0 == "Сколько это стоит? И как оплатить?" and content_0 == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        assert title_1 == "Хочу сразу несколько самокатов! Так можно?" and content_1 == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        assert title_2 == "Как рассчитывается время аренды?" and content_2 == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        assert title_3 == "Можно ли заказать самокат прямо на сегодня?" and content_3 == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        assert title_4 == "Можно ли продлить заказ или вернуть самокат раньше?" and content_4 == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        assert title_5 == "Вы привозите зарядку вместе с самокатом?" and content_5 == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        assert title_6 == "Можно ли отменить заказ?" and content_6 == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        assert title_7 == "Я жизу за МКАДом, привезёте?" and content_7 == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @allure.title('Проверка перехода по клику на логотип "Самокат"')
    def test_logo_scooter(self, driver):
        # создали объект класса главной страницы
        main_page = MainPage(driver)
        # открыли тестовую страницу
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        # кликнули на лого "Самокат" в шапге страницы
        main_page.click_on_logo_scooter()
        # проверили, что загрузилась главная страница "Яндекс Самокат"
        assert "Самокат" and "на пару дней" in main_page.check_home_page_scooter_visible()

    @allure.title('Проверка перехода по клику на логотип "Яндекс"')
    def test_logo_yandex(self, driver):
        # создали объект класса главной страницы
        main_page = MainPage(driver)
        # открыли тестовую страницу
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        # кликнули на лого "Яндекс" в шапге страницы
        main_page.click_on_logo_yandex()
        # проверили, что загрузилась главная страница "Яндекс Дзен"
        current_url = main_page.check_home_page_yandex_visible(1)
        assert current_url == 'https://dzen.ru/?yredirect=true'
