# Учебный проект в рамках курса "Python-разработчик" от ЯндексПрактикум. Сервис YaCut.

## Задачи проекта:
### Написать сервис укорачивания ссылок и API к нему.
#### Возможности сервиса :
- Генерация коротких ссылок и связь их с исходными длинными ссылками.
- Переадресация на исходный адрес при обращении к коротким ссылкам.
---
## Назначение проекта:
- Ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
### Запуск проекта в dev-режиме:

- Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/VictorAntropov/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Запустить проект из командной строки:
```
flask db init
flask db migrate -m 'Base'
flask db upgrade
flask run
http://127.0.0.1:5000
```

##  Автор проекта:
### Антропов Виктор:
```
e-mail: antropovvic1997@yandex.ru
GitHub: github.com/VictorAntropov
```