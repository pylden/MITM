from module.protocol.network.message import Message


class MapFightCountMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7990
        self.fightCount = {"type": "uint", "value": ""}
