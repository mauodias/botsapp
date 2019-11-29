class WhatsApp:
    def __init__(self):
        self._url = "https://web.whatsapp.com"
        self._chat_name = ''

    def initialize(self):
        pass

    @property
    def chat_name(self):
        if self._chat_name == '':
            raise Exception('Chat name not set.')
        return self._chat_name

    @chat_name.setter
    def chat_name(self, name):
        self._chat_name = name

    def get_messages(self, count=5):
        chat = self.chat_name
        return 'Yes'

    def send_message(self, message):
        chat = self.chat_name
        return 'Yes'
