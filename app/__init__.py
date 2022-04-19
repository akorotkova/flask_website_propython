from flask import Flask
from config import Config
from .main import main

# создание экземпляра приложения с текущими конфигурациями
app = Flask(__name__)
app.config.from_object(Config)

# регистрация блюпринта
app.register_blueprint(main)

# проверка верной текущей конфигурации приложения
for key, value in app.config.items():
    print(f'{key}: {value}')
print(app.config['DEBUG'])
print(app.config['SECRET_KEY'])
