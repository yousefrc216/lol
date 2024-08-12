import telebot, time, threading, json, random, re, os
from telebot import types
from chk1 import *
from bin import *

user = '6429416876'
admin_id = '6429416876'
token = "7213368243:AAGQGP9cQK0UwCaJ8tRLbpOxYEV6umPXI-A"
bot = telebot.TeleBot(token, parse_mode="HTML")

stop_processes = {}

video_urls = [
    "https://t.me/O_An6/106",
    "https://t.me/O_An6/110",
    "https://t.me/O_An6/111",
    "https://t.me/O_An6/112",
    "https://t.me/O_An6/113",
    "https://t.me/O_An6/114",
    "https://t.me/O_An6/118",
    "https://t.me/O_An6/119",
    "https://t.me/O_An6/120",
    "https://t.me/O_An6/121",
    "https://t.me/O_An6/123",
    "https://t.me/O_An6/124",
    "https://t.me/O_An6/126",
    "https://t.me/O_An6/129",
    "https://t.me/O_An6/131",
    "https://t.me/O_An6/132",
    "https://t.me/O_An6/133",
    "https://t.me/O_An6/136",
    "https://t.me/O_An6/137",
    "https://t.me/O_An6/208",
    "https://t.me/O_An6/717",
    "https://t.me/O_An6/722"
]

riskbins = []

def process(message):
    video_url = random.choice(video_urls)
    process_id = hash(message)
    stop_processes[process_id] = False
    dd = 0
    live = 0
    risko = 0
    stopped = False
    send = bot.send_video(message.chat.id, video_url, caption="𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬...⌛", parse_mode='Markdown', reply_to_message_id=message.message_id)
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = f"combo_{message.chat.id}.txt"
    
    try:
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception as o:
        bot.send_message(admin_id, f"An error occurred: {o}")
        return

    with open(file_name, 'r') as file:
        lino = file.readlines()
        total = len(lino)

        for card in lino:
            if card[:6] in riskbins:
                continue
            else:
                start_time = time.time()
                brand, type, level, bank, country_name, country_flag = info(card)
                try:
                    result = chk(card)
                except Exception as e:
                    bot.send_message(admin_id, f"An error occurred: {e}")
                    result = "ERROR"
                elapsed_time = round(time.time() - start_time, 2)
                print(result)
                card = card.replace('\n', '')
                    
                if any(keyword in result for keyword in ['funds', 'OTP', 'Charged', 'Funds', 'avs', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate', 'Successful', 'Authentication Required', 'successful', 'Thank you', 'confirmed', 'successfully', 'Thank you for your order', 'Insufficient Funds', 'Card Issuer Declined CVV', 'Payment Successfull', 'Your Payment Success', 'Douple Approved', 'Thank you for your order.', 'CVC check fails', 'CVV.', 'CVV', 'cvv', 'cvv.']):
                    live += 1
                    bot.reply_to(message, f'𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Auth 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href="tg://openmessage?user_id=6429416876">yousef</a>', parse_mode='HTML')
                elif 'RISK' in result:
                    risko +=1
                    riskbins.append(card[:6])
                else:
                    dd +=1

                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"{card}", callback_data='1', align_center=True)
                status = types.InlineKeyboardButton(f"{result}", callback_data='2')
                cm3 = types.InlineKeyboardButton(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ : {live}", callback_data='3')
                cm5 = types.InlineKeyboardButton(f"𝐑𝐢𝐬𝐤 ❌️ : {risko}", callback_data='4')
                cm6 = types.InlineKeyboardButton(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {dd}", callback_data='5')
                cm7 = types.InlineKeyboardButton(f"𝐓𝐨𝐭𝐚𝐥 🍬 : {total}", callback_data='6')
                stop_button = types.InlineKeyboardButton("𝐒𝐭𝐨𝐩", callback_data=f'stop_process_{process_id}')
                mes.add(cm1, status, cm3, cm5, cm6, cm7, stop_button)

                bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption=" ")
                bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=send.message_id, reply_markup=mes)

                for _ in range(25):
                    if stop_processes.get(process_id):
                        bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
                        riskbins.clear()
                        return
                    time.sleep(1)

    bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
    riskbins.clear()



@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_process'))
def stop_process_callback(call):
    process_id = call.data.split('_')[-1]
    stop_processes[int(process_id)] = True
    bot.answer_callback_query(call.id, "Process will be stopped.")
    
@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) not in [user]:
        return
    threading.Thread(target=process, args=[message]).start()

@bot.message_handler(commands=['start'])
def start_command(message):
    if str(message.chat.id) not in [user]:
        return   
    video_url = random.choice(video_urls)
    bot.send_video(message.chat.id, video_url, caption="𝐉𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐜𝐨𝐦𝐛𝐨", parse_mode='Markdown', reply_to_message_id=message.message_id)

bot.infinity_polling()