
import logging

from aiogram import Bot
from datetime import date
from lexicon.lexicon import LEXICON, LEXICON_YELLS, LEXICON_TRAININGS
from keyboards.training_kb import create_asking_keyboard

from keyboards.training_kb import create_asking_keyboard

logger = logging.getLogger(__name__)


def send_statistics() -> str:
    pass


async def send_morning_ask(bot: Bot):
    await bot.send_message(583465710,
                           LEXICON['ask_training'],
                           reply_markup=create_asking_keyboard())


def save_training(category: str):
    try:
        answer = f'{LEXICON["saved"]} {LEXICON_TRAININGS[category]} - {date.today()}'
    except:
        answer = LEXICON['already_exist']

    return answer


print(save_training('legs'))
