import asyncio

from aiogram import Bot, Dispatcher, executor, types
from styles import markup_start, markup_list_product, remove_markup
bot = Bot("6150506302:AAGOZY0QEuuw7QeJ189-kdHdNE7ZUOL8dCI")
dp = Dispatcher(bot)
print("BOT WAS STARTED")
import random

my_id = 972199181

@dp.message_handler(commands=["start"])
async def start(message):
    
    await bot.send_message(my_id, f"Кто-то зашёл сюда.{message}")
    await message.answer(f"<b>Здравствуйте, {message.from_user.first_name}!</b> Вы попали в лучший магазин <u>яблок</u> на этой планете!"
                         f" Следуйте инструкциям ниже и вы точно оформите заказ на моментальную доставку!", parse_mode="HTML", reply_markup= markup_start )

@dp.message_handler()
async def also_messages(message):
    if "Антоновка" in message.text or "Голден" in message.text or "Хоней Крисп" in message.text or "Хоней Крисп"  in message.text or "Ренет Симиренко"  in message.text:
        list_sort = ["Антоновка", "Голден", "Хоней Крисп", "Ренет Симиренко"]
        if message.text in list_sort:
            await message.answer(f"Если бы это был настоящий бот настоящего сервиса заказа яблок, то он обязательно добавил в БД заказ на килограммчик яблок {message.text}. Но увы, вся надежда только на вас :)", reply_markup= remove_markup)
        else:
            if "Хоней Крисп" in message.text or "Ренет Симиренко" in message.text:
                mess = message.text.split()
                sort = f"{mess[0]} {mess[1]}"
                try:
                    kilogram = int(mess[2])

                except Exception as ex:
                    print(ex)
                    await message.answer(
                    "Вы ввели неправильный формат килограммов. Не унывайте и попробуйте вновь! Уточню, нужно указывать только <b>ЦЕЛОЕ</b> число. Если дело совсем гиблое, воспользуйте нашей Техподдержкой.",
                    parse_mode="HTML")
            else:
                try:
                    sort, kilogram = message.text.split()
                except Exception as ex:
                    print(ex)
                    await message.answer(
                        "Вы ввели неправильный формат строчки. Не унывайте и попробуйте вновь! Если дело совсем гиблое, воспользуйте нашей Техподдержкой.")
            if sort in list_sort:
                try:
                    kilogram = int(kilogram)
                    await message.answer(f"Если бы это был настоящий бот настоящего сервиса заказа яблок, то он обязательно добавил в БД заказ яблок {sort} в количество {kilogram}кг. Но увы, вся надежда только на вас :)", reply_markup= remove_markup)
                except Exception as ex:
                    print(ex)
                    await message.answer(
                        "Вы ввели неправильный формат килограммов. Не унывайте и попробуйте вновь! Уточню, нужно указывать только <b>ЦЕЛОЕ</b> число. Если дело совсем гиблое, воспользуйте нашей Техподдержкой.", parse_mode= "HTML")
            else:
                await message.answer(
                    "Вы ввели неправильный формат строчки. Не унывайте и попробуйте вновь! Если дело совсем гиблое, воспользуйте нашей Техподдержкой.")


@dp.callback_query_handler()
async def callbackdata(call):
    if call.message:
        print(call)
        if call.data == "list_product":
            await bot.send_message(call['from'].id, text = f"Отлично, у нас в наличии:"
                                                        f"\nАнтоновка: {random.randrange(1,1000)}кг."
                                                        f"\nГолден: {random.randrange(1,1000)}кг."
                                                        f"\nХоней Крисп: {random.randrange(1,1000)}кг."
                                                        f"\nРенет Симиренко: {random.randrange(1,1000)}кг."
                                                        f"\nТо что понравилось смело добавляйте в корзину с помощью кнопок снизу!"
                                                        f" Стандартный шаг выбора -- 1 килограмм, если вы хотите больше, то впишите сорт яблок и через пробел количество килограмм.", parse_mode= "HTML", reply_markup= markup_list_product)
        elif call.data == "find_courier":
            await bot.send_message(call['from'].id, text = "Секунду, сейчас получу доступ к воображаемой БД")
            await asyncio.sleep(3)
            await bot.send_message(call['from'].id, text="Я совру, но курьер скоро будет у вашего дома :)")
        elif call.data == "trash_box":
            await bot.send_message(call['from'].id, text="Секунду, сейчас получу доступ к воображаемой БД")
            await asyncio.sleep(3)
            await bot.send_message(call['from'].id, text="Я совру, но ваша корзина набита до отказу :)")
executor.start_polling(dp, on_startup=print("Бот перезапустился"))