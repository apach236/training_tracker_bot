
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from random import choice
from database.database import user_db
from filters.filters import category_filter
from keyboards.training_kb import create_asking_keyboard, create_trainings_keyboard
from lexicon.lexicon import LEXICON, LEXICON_YELLS
from services.services import send_statistics, save_training

router = Router()

# Need to change to check in DB!!!
# Need to create ask_training by function!!! And check if trainings today


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
    await message.answer(text=LEXICON['ask_training'],
                         reply_markup=create_asking_keyboard())


@router.message(Command(commands='statistics'))
async def process_statistics_command(message: Message):
    await message.answer(text=f'{LEXICON[message.text]} {send_statistics()}')


@router.callback_query(F.data == 'yes')
async def send_trainings_keyboard(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON['which_training'],
        reply_markup=create_trainings_keyboard()
    )


@router.callback_query(F.data == 'no')
async def answer_no_trainings(callback: CallbackQuery):
    await callback.answer(choice(LEXICON_YELLS['shame']))


@router.callback_query(F.data == 'cancel')
async def process_cancel_button(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON['ask_training'],
        reply_markup=create_asking_keyboard()
    )


@router.callback_query(category_filter)
async def process_training_category(callback: CallbackQuery):
    await callback.message.edit_text(save_training(callback.data))
    await callback.answer(choice(LEXICON_YELLS['motivation']))
