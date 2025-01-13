from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.keys import Keys



class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = DataProvider().get('base_url')
        self.__driver = driver

    @allure.step("Перейти на сайт")
    def go(self):
        self.__driver.get(self.__url)


    @allure.step("Авторизоваться под {email}:{password}")
    def login_as(self, email: str, password: str):
        # Закрываем рекламный банер
        # WebDriverWait(self.__driver, 10).until(
            # EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tid="d6ef5dc"]'))).click()

        # Кликаем по кнопке "Войти"
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.styles_loginButton__LWZQp'))).click()

        # Ввод логина
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#passp-field-login"))).send_keys(email)

        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        # Ввод пароля
        WebDriverWait(self.__driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#passp-field-passwd"))).send_keys(password)

        self.__driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

        # Убеждаемся что главная страница загружена
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'[id="__next-route-announcer__"]')))
        # wait = WebDriverWait(self.__driver, 10)
        # wait.until(EC.visibility_of_element_located((By.XPATH, "/html")))


    @allure.step("Получить имя пользователя")
    def get_account_name(self):
        ActionChains(self.__driver).move_to_element(WebDriverWait(self.__driver, 50).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[class="styles_root__42Fk8"]')))).perform()
        menu = WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="styles_primaryTitle__lGNUB styles_primaryTitleDefaultAccount__a0_6V"]'))).text
        return menu

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.__driver.current_url

    @allure.story("Поиск фильма по названию")
    def search_movie_by_title(self, title):
        search_bar = self.__driver.find_element(By.CSS_SELECTOR, "[placeholder='Фильмы, сериалы, персоны']")
        search_bar.send_keys(title)
        search_bar.send_keys(Keys.RETURN)

        movie_link = WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, title))
        )
        movie_link.click()

        movie_title = self.__driver.find_element(By.CSS_SELECTOR, "[itemprop='name']").text

        return movie_title

    @allure.story("Добавление фильма в 'Буду смотреть'")
    def add_to_favorites(self):
        # Добавляем
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[title='Буду смотреть']"))).click()

        # Переходим в "Буду смотреть"
        self.__driver.find_element(By.CSS_SELECTOR, '[class="styles_filmsToWatchButton__r_vSy"]').click()