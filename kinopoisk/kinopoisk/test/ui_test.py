import allure
import pytest
from time import sleep

from kinopoisk.kinopoisk.test.page.MainPage import MainPage


#@pytest.mark.skip()
def test_auth(browser, test_data:dict):
    email = test_data.get('email')
    password = test_data.get('password')
    url = test_data.get('base_url')
    username = "Виктор Туманов"

    main_page = MainPage(browser)
    main_page.go()
    main_page.login_as(email, password)

    name = main_page.get_account_name()
    sleep(5)
    with allure.step("Имя пользователя должно быть "+username):
        assert name == username
    current_url = main_page.get_current_url()
    with allure.step("Проверить, что мы на странице "+current_url):
        assert main_page.get_current_url().startswith(url)

# @pytest.mark.skip()
# def test_first(browser):
#     cookie = {
#         'name': "Session_id",
#         'value': "3:1735059982.5.0.1735059982303:5eqNuQ:25f4.1.2:1|2061946799.0.2.3:1735059982|3:10300155.138552.AJEqhzP0gsitAAvypdOcU2OAnTU"
# }
#     main_page = MainPage(browser)
#     main_page.auth(cookie)
#

def test_search_movie_by_title(browser, test_data:dict):
    title = test_data.get('movie_title')
    movie_year = test_data.get("movie_release_date")
    main_page = MainPage(browser)
    main_page.go()
    search = main_page.search_movie_by_title(title)

    assert search == f"{title}{' '}{movie_year}"
    sleep(5)

def test_add_to_favorites(browser, test_data:dict):
    email = test_data.get('email')
    password = test_data.get('password')
    title = test_data.get('movie_title')

    main_page = MainPage(browser)
    main_page.go()
    main_page.login_as(email, password)
    main_page.search_movie_by_title(title)
    main_page.add_to_favorites()
    sleep(5)