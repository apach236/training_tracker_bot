
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from database.database import user_db
from keyboards.training_kb import create_asking_keyboard, create_trainings_keyboard
from lexicon.lexicon import LEXICON
from services.services import send_statistics, send_motivation, send_shame

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = {}
    await message.answer(text=LEXICON['ask_training'],
                         reply_markup=create_asking_keyboard())


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='statistics'))
async def process_statistics_command(message: Message):
    await message.answer(text=f'{LEXICON[message.text]} {send_statistics()}')

# functions do not work! Need to change message by callback


@router.callback_query(F.data == 'Yes')
async def send_trainings_keyboard(callback: CallbackQuery):
    await callback.answer(text=send_motivation())


@router.callback_query(F.data == 'No')
async def answer_no_trainings(callback: CallbackQuery):
    await callback.answer(text=send_shame())
