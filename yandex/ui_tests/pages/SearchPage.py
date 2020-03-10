#!/usr/bin/python3
from yandex.ui_tests.pages.Base import Base
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:

    SEARCH_FIELD = (By.ID, "text")
    VARIANTS_REQUEST = (By.CLASS_NAME, "suggest2-item__text")
    TEMPERATURE = (By.CLASS_NAME, "suggest2-item__fact")
    LOTO_LINK = (By.CSS_SELECTOR, "div.popup__content")


class YandexSearchPage(Base):

        def open_site(self):
            self.driver.get(self.yandex_url)

        def set_request(self, text):
            print(f'Search text: {text}')
            input_search = self.driver.find_element(*YandexSeacrhLocators.SEARCH_FIELD)
            input_search.send_keys(text)

        def select_first_variant(self, text):
            variant_first = self.driver.find_element(*YandexSeacrhLocators.VARIANTS_REQUEST).text
            if text == 'Погода':
                temperature = self.driver.find_element(*YandexSeacrhLocators.TEMPERATURE).text
                print(f'First variant: {variant_first} {temperature}')
            elif text == 'Лото':
                loto_link = self.driver.find_element(*YandexSeacrhLocators.LOTO_LINK).text
                print(f'First variant: {loto_link[:70]}')
            else:
                print(f'First variant: {variant_first}')

        def clear_request(self):
            input_search = self.driver.find_element(*YandexSeacrhLocators.SEARCH_FIELD)
            input_search.clear()
