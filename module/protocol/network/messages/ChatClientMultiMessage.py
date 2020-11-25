from module.protocol.network.message import Message


class ChatClientMultiMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5022
        self.channel = {"type": "uint", "value": ""}
