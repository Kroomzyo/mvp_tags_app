# MVP_miniapp ✨

![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXZ1HdcemOZFjtx5Vk-kK_AYiQkBPTNSKk9bRuYXLHg_4HW5Y35AQuNmiOlcFHLASOaMA&usqp=CAU)

Boiler_plate_for_mini_apps — шаблон для обработки тегов при переходе в mini_app.

## Контакты
Если у вас есть вопросы, напишите мне в Telegram:  
👉 [Перейти в Telegram](https://t.me/kroomzz)

## Содержание🐱‍👤

- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)
- [Конфигурация](#конфигурация)
  

## Описание
Минимально работоспособный продукт

## Установка 🛠️
- Для развертывания контейнера выполнить:
1) git clone репозитория
2) сd репозиторий
3) docker build -t название_app .
4) docker run -d -p порт:порт -e BOT_TOKEN="ваш-bot-token" название_app

   
### Предварительные требования
- Всё в Dockerfile/requirements.txt

### Установка зависимостей
- Всё в Dockerfile/requirements.txt


## Использование
- Докер распаковывает папку project, поэтому для запуска локально необходимо:
1) Добавить к импортам модуль project.
2) Создать файл .env в корне проекта и внести свой BOT_TOKEN в формате: `BOT_TOKEN="token"`
3) Выполнить первоначальную [конфигурацию](#конфигурация)
4) Запустить `main.py`

## Конфигурация
- Первоначальная конфигурация находится в `config.settings.py`:
```python
class Settings(BaseSettings):
    BOT_TOKEN: str
    PHOTO_HELLO_ID: str = "photo_id"
    BASE_URL_INFO: str = "url_1"
    BASE_URL_DOCS: str = "url_2"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
```
- Касаемо URL всё прозрачно - необходимо вставить ссылки на URL в указанные поля (возможно использование через .env)
В случае если вы хотите использовать PHOTO_HELLO_ID через бота, необходимо в handlers.start_handler раскомментировать:
```python
@router.message(F.photo)
async def get_photo_id(message: Message):
     await message.answer(f"FileID: {message.photo[-1].file_id}")
```
После чего отправить фото боту, он в ответ вернет id фотографии уже с серверов Telegram. Это id необходимо вставить в параметр PHOTO_HELLO_ID,
для его корректного использования ботом, после чего перезагрузить его.
Затем предыдущий кусок кода можно закомментировать/утилизировать.

- Логирование убрано для чистоты


