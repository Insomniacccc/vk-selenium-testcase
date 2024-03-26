import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys

class TestYandexSearch:

    @pytest.fixture(scope="class")
    def setup(self):
        driver = webdriver.Chrome()
        driver.get('https://ya.ru/')
        yield driver
        driver.quit()

    def test_yandex_search(self, setup):
        """
                Тест-кейс: Поиск слова "Selenium" на первой позиции поисковика Yandex
                id: 0001

                Шаги:
                1. Открыть браузер и перейти на страницу ya.ru
                2. Ввести "Selenium" в поле поиска
                3. Нажать клавишу Enter или кнопку поиска
                4. Дождаться загрузки результатов поиска
                5. Проверить, что слово "Selenium" находится на первой позиции в результатах поиска

                Ожидаемый результат: Слово "Selenium" находится на первой позиции в результатах поиска
        """

        search_input = setup.find_element(By.CSS_SELECTOR, 'input[name="text"]')
        search_input.send_keys("Selenium")
        search_input.send_keys(Keys.ENTER)

        WebDriverWait(setup, 10).until(expect.visibility_of_element_located((By.CSS_SELECTOR, 'li.serp-item')))
        search_results = setup.find_elements(By.CSS_SELECTOR, 'li.serp-item')
        first_result_text = search_results[0].text.lower()

        assert "selenium" in first_result_text, "Слово 'Selenium' не найдено на первой позиции в результатах поиска"

