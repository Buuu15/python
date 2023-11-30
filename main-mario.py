from telegram import Update
from telegram.ext import Application, CommandHandler, filters, MessageHandler, ContextTypes

key_token = "6981725882:AAHEWh7IUH3h6ICvJ3-esvGiR3KrPtuSvMg"
user_bot = "@tedx_bot"

async def start_cmd(update: Update, context):
    await update.message.reply_text("Hi! Thanks for chatting with me, my name is ted. Please type /help to see my command list")

async def help_cmd(update: Update, context):
    await update.message.reply_text("This is my command list:\n1. Hello\n2. What is your name?\n3. What is your function?\n4. what is the formula for the perimeter of a square?\n5. What is the formula for the perimeter of a rectangle?")

def handle_response(text: str):
    processed: str = text.lower()
    if 'hello' in processed:
        return "Hi"
    elif 'what is your name' in processed:
        return f"My name is {user_bot}, I'm a bot made by Buuu"
    elif 'what is your function?'in processed:
        return "My function is to remind you about math formulas"
    elif 'what is the formula for the perimeter of a square?' in processed:
        return "The formula for the perimeter of a square is 4 x side"
    elif 'what is the formula for the perimeter of a rectangle?' in processed:
        return "The formula for the perimeter of a rectangle is p = (L + w) x 2"

    return "I don't understand what you're trying to say"

async def handle_message(update: Update, context):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if user_bot in text:
            new_text: str = text.replace(user_bot, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)

async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Nice picture")

async def error(update: Update, context):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print("Start")
    app = Application.builder().token(key_token).build()
    # COMMAND :
    app.add_handler(CommandHandler('start', start_cmd))
    app.add_handler(CommandHandler('help', help_cmd))
    # MESSAGE:
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # ERROR:
    app.add_error_handler(error)
    # POLLING:
    app.run_polling(poll_interval=1)
