#!/usr/bin/python3
import pytest
from yandex.ui_tests.pages.SearchPage import YandexSearchPage


class TestYandexSearch:

    search_text = ['Погода', 'Липецк', 'Лото']

    @pytest.mark.parametrize("text", search_text)
    def test_select_variant_search(self, text, driver):
        search_page = YandexSearchPage(driver)
        search_page.open_site()
        search_page.set_request(text)
        search_page.select_first_variant(text)
        search_page.clear_request()
        driver.quit()
