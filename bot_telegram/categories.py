from telegram import InlineKeyboardButton

class Categories:

    category_dict = {
        'b_missing_tree': 'Mark location as To Plant',
        'b_stump': 'Mark location as a Stump',
        'b_dead_tree': 'Mark location as Dead Tree',
        'b_dead_sapling': 'Mark location as Dead Sapling'
    }

    @classmethod
    def get_keyboard(cls):
        inline_keyboard = []
        for ckey, cvalue in cls.category_dict.items():
            inline_keyboard.append([InlineKeyboardButton(cvalue, callback_data=ckey)])
        return inline_keyboard

    @classmethod
    def get_handler(cls):
        pass

    @classmethod
    def get_pattern(cls):
    #pattern=Categories.category_dict.keys() "^(b_missing_tree|b_stump|b_dead_tree|b_dead_sapling)$`")
        return "^("+"|".join(cls.category_dict.keys())+")$"