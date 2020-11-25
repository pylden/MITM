from module.protocol.network.message import Message


class GuildPaddockBoughtMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9535
        self.paddockInfo = {"type": "PaddockContentInformations", "value": ""}
