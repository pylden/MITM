from module.protocol.network.message import Message


class ChatClientPrivateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9769
        self.receiver = {"type": "String", "value": ""}
