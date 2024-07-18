# Погода в городе любви

### Описание проекта
"Погода в городе любви" — это веб-сервис, который позволяет пользователям получить информацию о погоде в Париже.

### Технологии
![](https://img.shields.io/badge/Python-blue?logo=Python&logoColor=yellow&style=for-the-badge)
![](https://img.shields.io/badge/Django-092e20?logo=Django&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/poetry-ad998b?logo=poetry&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/docker-blue?logo=docker&logoColor=white&style=for-the-badge)
![](https://img.shields.io/badge/gunicorn-white?logo=gunicorn&logoColor=%23092E20&style=for-the-badge)

### Разработчик
[Никита Сенгилейцев](https://github.com/NikAfraim)

## Запуск проекта

### Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/NikAfraim/weather_paris.git
```

2. Перейдите в каталог проекта:
```bash
cd weather_paris
```

3. Создайте файл .env в `/weather_site`, используя шаблон `/weather_site/.env.example`.


### Запуск

1. Перейдите в `infra/`:
```bash
cd infra/
```

2. Запустите docker-compose:
```bash
docker compose up -d --build
```

Проект будет доступен по адресу: http://localhost/.