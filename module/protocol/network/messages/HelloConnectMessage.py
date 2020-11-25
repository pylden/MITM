from module.protocol.network.message import Message


class HelloConnectMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2607
        self.salt = {"type": "String", "value": ""}
        self.key = {"type": "Vector.<int>", "value": ""}
