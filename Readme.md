# Blog comment system
Тестовое задание в команду "Квартирка" (Junior Python Разработчик)

 [ПРОЕКТИРОВАНИЕ БД](https://drive.google.com/file/d/1MBpDzxMBGHr5QQwQ3mZeQAZXjIrCvgBm/view?usp=sharing)
 
# Инструкция по запуску
1. `python3 -m venv venv` - инициализация виртуального окружения
2. `source venv/bin/activate` - вход в виртуальное окружение
3. `pip install -r requirements.txt` - установка зависимостей
4. `docker-compose up -d ` - поднятие базы данных (если установлен Docker)
5. `python src/manage.py migrate` - запуск миграций
6. `python src/manage.py runserver` - запуск приложения

## Дополнительные задания
1. Docker и Docker-compose файлы
2. Postgres
