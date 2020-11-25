from module.protocol.network.message import Message


class AcquaintanceServerListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 137
        self.servers = {"type": "Vector.<uint>", "value": ""}
