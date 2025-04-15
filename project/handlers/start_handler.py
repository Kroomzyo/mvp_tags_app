from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from config.settings import settings
from services.url_service import UrlService
from services.text_service import TextService
from keyboards.inline import InlineKeyboards

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message):

    payload = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else ""
    utm_params = UrlService.parse_start_parameters(payload)

    keyboard = InlineKeyboards.start_keyboard(utm_params).as_markup()
    text = TextService.get_welcome_text(message.from_user.first_name)

    await message.answer_photo(
        photo=settings.PHOTO_HELLO_ID,
        caption=text,
        reply_markup=keyboard
    )

# Для получения фото id ->

# @router.message(F.photo)
# async def get_photo_id(message: Message):
#     await message.answer(f"FileID: {message.photo[-1].file_id}")
