# vk-selenium-testcase
Test case for VK internship

Тест-кейс: Поиск слова "Selenium" на первой позиции поисковика Yandex
                id: 0001

                Шаги:
                1. Открыть браузер и перейти на страницу ya.ru
                2. Ввести "Selenium" в поле поиска
                3. Нажать клавишу Enter или кнопку поиска
                4. Дождаться загрузки результатов поиска
                5. Проверить, что слово "Selenium" находится на первой позиции в результатах поиска

                Ожидаемый результат: Слово "Selenium" находится на первой позиции в результатах поиска

Browser: Google Chrome 123.0.6312.59(Official build)
Python 3.9
Pytest 7.2.2
Selenium Webdriver 4.8.2
