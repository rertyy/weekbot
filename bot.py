
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater, ContextTypes, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.parsemode import ParseMode
from datetime import datetime, timedelta, date 
from math import floor


TOKEN = "5588939107:AAHAmlveATn-7sHpAIN4sqLu8PJqlxK8dLA"





updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)





def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=
                             "This bot hopes you tell you the week number but most likely has bugs.\n"
                             "/weeknum: shows the current week number \n"
                             "/help: shows helps\n"
                             "/start: start from the beginning"
                             )


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=
                             "You pitaya"
                             )

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

#Today
def today(update: Update, context: CallbackContext):
    date_today=date.today().strftime('%d.%m.%Y')
    context.bot.send_message(chat_id=update.effective_chat.id, text=
                                 f"Today is {date_today} (DD.MM.YYYY)\n")
                             


today_handler = CommandHandler('today', today)
dispatcher.add_handler(today_handler)


today = date.today()
print(f"today is {today}")
#today=date(2022,10,8)
weekOne = date(2022,8,8) #insert Monday of week 0 semester here YYYY,MM,DD
weekOne=weekOne - timedelta(days=7)
print(today)
semester="2022/23 Sem1"
mondayOne = (weekOne - timedelta(days=weekOne.weekday())) 
mondayThis = (today - timedelta(days=today.weekday()) )

#Weeknum
def weeknum(update: Update, context: CallbackContext):
    date_today=date.today().strftime('%d.%m.%Y')
    context.bot.send_message(chat_id=update.effective_chat.id, text=
                                 f"Today is {date_today} (DD.MM.YYYY)\n")

    if today<weekOne:
        print("sem not started")
        daysLeft =(weekOne-today).days
        print(f"{daysLeft} days until Sunday of Week 1")
        context.bot.send_message(chat_id=update.effective_chat.id, text=
                                 f"{semester} has not started.\n"
                                 f"{daysLeft} days until Week 1 starts"
                                 )
    else:
        weekDiff = floor((mondayThis - mondayOne).days / 7)
        if weekDiff==7:
            weekDiff="Reading Week"
        elif weekDiff>7 and weekDiff<=14:
            weekDiff-=1
        elif weekDiff>14:
            weekDiff=">13"
        print(f"It is now week {weekDiff}")
        context.bot.send_message(chat_id=update.effective_chat.id, text=
                                f"It is now week {weekDiff}"
                                )
        context.bot.send_message(chat_id=update.effective_chat.id, text=
                                 "Click <a href='google.com'>here</a> for calendar",
                                 parse_mode=ParseMode.HTML,
                                 )



weeknum_handler = CommandHandler('weeknum', weeknum)
dispatcher.add_handler(weeknum_handler)

'''
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
'''




def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()



