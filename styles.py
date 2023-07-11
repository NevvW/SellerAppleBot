from aiogram import types

remove_markup = types.ReplyKeyboardRemove()

item1_start = types.InlineKeyboardButton(text="Посмотреть список товаров 🍎", callback_data="list_product")
item2_start = types.InlineKeyboardButton(text="Где мой заказ? 🔎", callback_data="find_courier")
item3_start = types.InlineKeyboardButton(text="Посмотреть корзину 🧺", callback_data="trash_box")
item4_start = types.InlineKeyboardButton(text="Техподдержка 📞",url = "https://site.ru/support")
markup_start = types.InlineKeyboardMarkup(row_width=2)
markup_start.add(item1_start).add(item2_start, item3_start, item4_start)


item1_start = types.InlineKeyboardButton(text="Антоновка", callback_data="antonovka")
item2_start = types.InlineKeyboardButton(text="Голден", callback_data="golden")
item3_start = types.InlineKeyboardButton(text="Хоней Крисп", callback_data="honey_crisp")
item4_start = types.InlineKeyboardButton(text="Ренет Симиренко", callback_data="renet_simorenko")
markup_list_product = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_list_product.add(item1_start,item2_start, item3_start, item4_start)