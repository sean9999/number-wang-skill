from mycroft import MycroftSkill, intent_file_handler


class NumberWang(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wang.number.intent')
    def handle_wang_number(self, message):
        self.speak_dialog('wang.number')


def create_skill():
    return NumberWang()

