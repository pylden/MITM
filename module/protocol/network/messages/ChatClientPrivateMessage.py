from module.protocol.network.message import Message


class ChatClientPrivateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9769
        self.receiver = {"type": "String", "value": ""}
