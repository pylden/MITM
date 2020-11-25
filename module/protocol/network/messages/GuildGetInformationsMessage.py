from module.protocol.network.message import Message


class GuildGetInformationsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3578
        self.infoType = {"type": "uint", "value": ""}
