
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, LEXICON_TRAININGS


def create_asking_keyboard() -> InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(InlineKeyboardButton(text=LEXICON['Yes'], callback_data='Yes'),
                   InlineKeyboardButton(
                       text=LEXICON['No'], callback_data='No'),
                   width=2)

    return kb_builder.as_markup()


def create_trainings_keyboard() -> InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []
    for button, category in LEXICON_TRAININGS.items():
        buttons.append(InlineKeyboardButton(
            text=category,
            callback_data=button))

    kb_builder.row(*buttons, width=1)

    return kb_builder.as_markup()
