from module.protocol.network.message import Message


class GuildPaddockBoughtMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9535
        self.paddockInfo = {"type": "PaddockContentInformations", "value": ""}
