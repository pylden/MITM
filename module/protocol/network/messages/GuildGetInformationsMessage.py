from module.protocol.network.message import Message


class GuildGetInformationsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3578
        self.infoType = {"type": "uint", "value": ""}
