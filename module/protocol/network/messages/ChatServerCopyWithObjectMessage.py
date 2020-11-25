from module.protocol.network.message import Message


class ChatServerCopyWithObjectMessage(Message):
    def __init__(self):
        self.id = 4706
