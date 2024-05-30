# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



# Инициализируем браузер
# driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://divan.ru/category/divany-i-kresla"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)

divans = driver.find_elements(By.CLASS_NAME, 'lcSMD')

# Выводим вакансии на экран
print(divans)
# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for divan in divans:
    try:

        # Находим названия дивана
        title = divan.find_element(By.CSS_SELECTOR, 'span.ui-GPFV8 qUioe ProductName ActiveProduct').text
        # Находим цену
        price = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        # Находим ссылку с помощью атрибута 'href'
        link = divan.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
        # Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
    except:
        print("произошла ошибка при парсинге")
        continue

    # Вносим найденную информацию в список
    parsed_data.append([title, price, link])



# Закрываем подключение браузер
driver.quit()



# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
with open("divans.csv", 'w', newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Название дивана', 'цена', 'ссылка на товар'])

    # Прописываем использование списка как источника для рядов таблицы
    writer.writerows(parsed_data)
