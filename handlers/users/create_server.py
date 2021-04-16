from typing import Union

from aiogram import types
# from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.inline.create_server_keyboards import categories_keyboard, select_tarif_line_keyboard, tarif_keyboard, \
    steps_data, select_os_or_app_keyboard, make_callback_data
from loader import dp


@dp.message_handler(Command('new_server'))
async def show_alert(message: types.Message):
    await select_os_or_app(message)


async def select_os_or_app(message: Union[CallbackQuery, Message], **kwargs):
    markup = await select_os_or_app_keyboard()
    if isinstance(message, Message):
        await message.answer("Образы", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def get_os_list(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()
    if isinstance(message, Message):
        await message.answer("Выбери ос", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def select_tarif_line(message: Union[CallbackQuery, Message], **kwargs):
    markup = await select_tarif_line_keyboard()
    if isinstance(message, Message):

        await message.answer(
            "Выбери тарифную сетку:\n\n"
            "Старт: VPS начального уровня для тестирования, разработки и хостинга сайтов. "
            "Производительность до 20% ниже, чем на тарифе Стандарт. \n\n"
            "Стандарт: Оптимальный уровень производительности для хостинга сайтов, "
            "баз данных и задач веб-разработки. \n\n"
            "Высокочастотные: Процессоры с базовой частотой 3,7+ ГГц и технологией Turbo Boost до 5 ГГц. "
            "До 40% производительнее, чем тарифы Стандарт. Рекомендуется для проектов на 1С-Битрикс.\n\n"
            "Выделенные: Отдельные хост-ноды с небольшим числом виртуальных серверов. "
            "Разрешена загрузка ядра процессора на 100% и повышенная нагрузка на диск.",
            reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


async def get_tarif_list(message: Union[CallbackQuery, Message], **kwargs):
    markup = await tarif_keyboard()
    if isinstance(message, Message):
        await message.answer("Выбери тариф", reply_markup=markup)
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


# Функция, которая обрабатывает ВСЕ нажатия на кнопки в этой менюшке
@dp.callback_query_handler(steps_data.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = callback_data.get("level")

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    get_os_list = callback_data.get("get_os_list")

    # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    get_tarif_list = callback_data.get("get_tarif_list")

    # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
    levels = {
        "0": get_os_list,  # Отдаем категории
        "1": get_tarif_list,  # Отдаем подкатегории
    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        get_os_list=get_os_list,
        get_tarif_list=get_tarif_list,

    )
