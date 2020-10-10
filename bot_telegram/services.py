import os

def save_coordinates(coordinates):
    print(coordinates)


def save_photo(update, context):
    update.message.reply_text("Saving photo")
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', f'{photo_file.file_id}.jpg')
    photo_file.download(filename)
    update.message.reply_text("File saved")


def save_category(category):
    print(category)