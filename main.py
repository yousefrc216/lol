import telebot
import time
import threading
import random
import datetime
from telebot import types
from chk1 import chk as chk1
from chk2 import chk as chk2
from chk3 import chk as chk3
from chk4 import chk as chk4
from chk5 import chk as chk5
from chk6 import chk as chk6
from bin import *
import hashlib

admin_ids = ['6429416876']
token = "7316200406:AAGc9gUoiKS8xZCI2i15B3tO4zpZjl6o7m0"
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
activation_codes = {}
authorized_users = {admin_ids[0]: float('inf')}

def generate_code(duration_hours):
    code = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    expiration_time = time.time() + duration_hours * 3600
    expiration_date = datetime.datetime.fromtimestamp(expiration_time).strftime('%Y-%m-%d %H:%M')
    activation_codes[code] = expiration_time
    return code, expiration_date

def generate_code_minutes(duration_minutes):
    code = hashlib.md5(str(random.random()).encode()).hexdigest()[:8]
    expiration_time = time.time() + duration_minutes * 60
    expiration_date = datetime.datetime.fromtimestamp(expiration_time).strftime('%Y-%m-%d %H:%M')
    activation_codes[code] = expiration_time
    return code, expiration_date

def process(document, message, chk_function):
    video_url = random.choice(video_urls)
    process_id = hash(message)
    stop_processes[process_id] = False
    dd = 0
    live = 0
    risko = 0
    send = bot.send_video(message.chat.id, video_url, caption="𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬...⌛", parse_mode='Markdown', reply_to_message_id=message.message_id)
    file_info = bot.get_file(document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = f"combo_{message.chat.id}.txt"
    
    try:
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
    except Exception as o:
        bot.send_message(admin_ids[0], f"An error occurred: {o}")
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
                    result = chk_function(card)
                except Exception as e:
                    bot.send_message(admin_ids[0], f"An error occurred: {e}")
                    result = "ERROR"
                elapsed_time = round(time.time() - start_time, 2)
                print(result)
                card = card.replace('\n', '')
                    
                if any(keyword in result for keyword in ['funds', 'OTP', 'Charged', 'Funds', 'avs', 'postal', 'approved', 'Nice!', 'Approved', 'cvv: Gateway Rejected: cvv', 'does not support this type of purchase.', 'Duplicate', 'Successful', 'Authentication Required', 'successful', 'Thank you', 'confirmed', 'successfully', 'Thank you for your order', 'Insufficient Funds', 'Card Issuer Declined CVV', 'Payment Successfull', 'Your Payment Success', 'Douple Approved', 'Thank you for your order.', 'CVC check fails', 'CVV.', 'CVV', 'cvv', 'cvv.']):
                    live += 1
                    bot.reply_to(message, f'𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Auth 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href="tg://openmessage?user_id=6429416876">Yousef 🔥</a>', parse_mode='HTML')
                elif 'RISK' in result:
                    risko += 1
                    riskbins.append(card[:6])
                else:
                    dd += 1

                buttons = types.InlineKeyboardMarkup(row_width=1)
                a1 = types.InlineKeyboardButton(f"{card}", callback_data='1')
                a2 = types.InlineKeyboardButton(f"{result}", callback_data='2')
                a3 = types.InlineKeyboardButton(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ : {live}", callback_data='3')
                a4 = types.InlineKeyboardButton(f"𝐑𝐢𝐬𝐤 ❌️ : {risko}", callback_data='4')
                a5 = types.InlineKeyboardButton(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {dd}", callback_data='5')
                a6 = types.InlineKeyboardButton(f"𝐓𝐨𝐭𝐚𝐥 🍬 : {total}", callback_data='6')
                stop_button = types.InlineKeyboardButton("𝐒𝐭𝐨𝐩", callback_data=f'stop_process_{process_id}')
                buttons.add(a1, a2, a3, a4, a5, a6, stop_button)
                
                bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=send.message_id, reply_markup=buttons)

                for _ in range(23):
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

@bot.callback_query_handler(func=lambda call: call.data.startswith('braintree_auth'))
def file_process_callback(call):
    message = call.message
    document = call.message.reply_to_message.document
    if call.data == 'braintree_auth_1':
        chk_function = chk1
    elif call.data == 'braintree_auth_2':
        chk_function = chk2
    elif call.data == 'braintree_auth_3':
        chk_function = chk3
    elif call.data == 'braintree_auth_4':
        chk_function = chk4
    elif call.data == 'braintree_auth_5':
        chk_function = chk5
    elif call.data == 'braintree_auth_6':  
        chk_function = chk6
    threading.Thread(target=process, args=[document, message, chk_function]).start()

@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) not in authorized_users:
        bot.reply_to(message, "You are not authorized to use the bot. Please provide a valid activation code.")
        return
    buttons = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Braintree Auth 1🔥", callback_data='braintree_auth_1')
    button2 = types.InlineKeyboardButton("Braintree Auth 2🔥", callback_data='braintree_auth_2')
    button3 = types.InlineKeyboardButton("Braintree Auth 3🔥", callback_data='braintree_auth_3')
    button4 = types.InlineKeyboardButton("Braintree Auth 4🔥", callback_data='braintree_auth_4')
    button5 = types.InlineKeyboardButton("Braintree Auth 5🔥", callback_data='braintree_auth_5')
    button6 = types.InlineKeyboardButton("Braintree Auth 6🔥", callback_data='braintree_auth_6')
    buttons.add(button1, button2, button3, button4, button5, button6)
    bot.reply_to(message, "Please choose an option:", reply_markup=buttons)

@bot.message_handler(commands=["vip"])
def start(message):
    bot.reply_to(message,'╔═══════════════\n╟✅𝗖𝗢𝗠𝗕𝗢 𝗕𝗼𝘁 𝗔𝗰𝗰𝗲𝘀𝘀   ⚡️ \n╚═══════════════\n╔═══════════════\n╟✅1️⃣ 𝗗𝗮𝘆 1$ 💸 \n╚═══════════════\n╔═══════════════\n╟✅5️⃣ 𝗗𝗮𝘆 3$💸 \n╚═══════════════\n╔═══════════════\n╟✅1️⃣ 𝗪𝗲𝗲𝗸 5$  💸 \n╚═══════════════\n╔═══════════════\n╟✅1️⃣ 𝗠𝗼𝗻𝘁𝗵  15$ 💸 \n╚═══════════════\n╔═══════════════\n╟✅𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲 𝗕𝘆 @Y_1_M_1 \n╚═══════════════')
 
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! Please send a file to start checking.")

@bot.message_handler(commands=['key'])
def generate_activation_code(message):
    if str(message.chat.id) not in admin_ids:
        bot.reply_to(message, "You are not authorized to generate activation codes.")
        return

    try:
        duration_hours = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, "Please provide the duration in hours. Usage: /key <hours>")
        return

    code, expiration_date = generate_code(duration_hours)
    bot.reply_to(message, f"🔥NEW KEY\n"
    f"━━━━━━━━━━━━━━━━━━\n"
    f"[✓]Use: /redeem\n"
    f"[✓]Key: {code}\n"
    f"[✓]Plan: VIP\n"
    f"[✓] Expiry: {expiration_date} تاريخ الانتهاء", parse_mode='HTML')

@bot.message_handler(commands=['key2'])
def generate_activation_code_minutes(message):
    if str(message.chat.id) not in admin_ids:
        bot.reply_to(message, "You are not authorized to generate activation codes.")
        return

    try:
        duration_minutes = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, "Please provide the duration in minutes. Usage: /code2 <minutes>")
        return

    code, expiration_date = generate_code_minutes(duration_minutes)
    bot.reply_to(message,  f"🔥NEW KEY\n"
    f"━━━━━━━━━━━━━━━━━━\n"
    f"[✓]Use: /redeem\n"
    f"[✓]Key: {code}\n"
    f"[✓]Plan: VIP\n"
    f"[✓] Expiry: {expiration_date} تاريخ الانتهاء", parse_mode='HTML')

@bot.message_handler(commands=['activate', 'redeem'])
def activate_code(message):
    try:
        code = message.text.split()[1]
    except IndexError:
        bot.reply_to(message, "Please provide an activation code. Usage: /activate <code>")
        return

    expiration_time = activation_codes.get(code)
    if not expiration_time:
        bot.reply_to(message, "Invalid activation code.")
        return

    if time.time() > expiration_time:
        bot.reply_to(message, "Activation code has expired.")
        return

    authorized_users[str(message.chat.id)] = expiration_time
    expiry_date = datetime.datetime.fromtimestamp(expiration_time).strftime('%Y-%m-%d')
    bot.reply_to(message, f"♻️ Key Redeemed Successfully, Welcome To Paid Membership\n━━━━━━━━━━━━━━━━━━\nUser: @{message.from_user.username}\nUserID: {message.from_user.id}\nRank: VIP\nExpiry Date: {expiry_date}\n━━━━━━━━━━━━━━━━━━")

def revoke_expired_codes():
    while True:
        current_time = time.time()
        expired_users = [user_id for user_id, expiration_time in authorized_users.items() if expiration_time <= current_time]
        for user_id in expired_users:
            del authorized_users[user_id]
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=revoke_expired_codes, daemon=True).start()
    bot.polling()
