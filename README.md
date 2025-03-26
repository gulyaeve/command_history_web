# Command History Web

Веб-приложение для отображения и управления историей команд.

## Описание

Это веб-приложение позволяет просматривать и управлять историей команд в удобном веб-интерфейсе. Приложение построено на Python с использованием Flask.

## Структура проекта

```
command_history_web/
├── command_history_server.py  # Основной серверный файл
├── requirements.txt          # Зависимости проекта
├── static/                  # Статические файлы (CSS, JS, изображения)
└── templates/              # HTML шаблоны
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone git@github.com:romatrooy/command_history_web.git
cd command_history_web
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

Для запуска приложения выполните:
```bash
python command_history_server.py
```

После запуска приложение будет доступно по адресу: `http://localhost:5000`

## Требования

- Python 3.x
- Зависимости из файла requirements.txt

## Лицензия

MIT License 