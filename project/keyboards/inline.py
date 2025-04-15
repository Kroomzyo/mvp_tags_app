from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, WebAppInfo
from config.settings import settings
from services.url_service import UrlService


class InlineKeyboards:
    @staticmethod
    def start_keyboard(utm_params: dict) -> InlineKeyboardBuilder:
        builder = InlineKeyboardBuilder()

        urls = [
            (settings.BASE_URL_INFO, 'Играть'),
            (settings.BASE_URL_DOCS, 'Официальные документы')
        ]

        for url, text in urls:
            web_app_url = UrlService.build_webapp_url(url, utm_params)
            builder.add(InlineKeyboardButton(
                text=text,
                web_app=WebAppInfo(url=web_app_url)
            ))

        builder.adjust(1)
        return builder
