from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext # type: ignore # no need to ignore type checking

TOKEN: Final = '7481900361:AAF0CA5igRkcDOkTFa9b5-l66MChZTJbgcs'
BOT_USER: Final = '@Techinfo_withme_bot'

# Commands
async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello, thanks for chatting with me! I am Techy.')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('I am Techy. Please type something so I can respond.')

async def custom_command(update: Update, context: CallbackContext):
    await update.message.reply_text('This is a custom command.')

async def language_info_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Here is some information about 5 different programming languages:\n'
        '1. Python: A high-level, interpreted language known for its readability and ease of use.\n'
        '2. JavaScript: A versatile, high-level language primarily used for web development.\n'
        '3. Java: A class-based, object-oriented language designed to be platform-independent.\n'
        '4. C++: An extension of C that includes object-oriented features, used in systems/software development.\n'
        '5. Ruby: An interpreted, high-level language known for its simplicity and productivity.'
    )

# Response handling
def handle_responses(text: str) -> str:
    processed = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'i love python' in processed:
        return 'Remember to subscribe!'
    return 'I do not understand what you wrote.'

async def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    response = handle_responses(text)
    await update.message.reply_text(response)

async def error(update: Update, context: CallbackContext):
    print(f"An error occurred: {context.error}")

def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('custom', custom_command))
    application.add_handler(CommandHandler('language_info', language_info_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Error Handler
    application.add_error_handler(error)

    # Run the bot
    print('Starting bot...')
    application.run_polling()

if __name__ == '__main__':
    main()
