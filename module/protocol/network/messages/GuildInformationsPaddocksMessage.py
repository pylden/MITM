from module.protocol.network.message import Message


class GuildInformationsPaddocksMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6791
        self.nbPaddockMax = {"type": "uint", "value": ""}
        self.paddocksInformations = {"type": "Vector.<PaddockContentInformations>", "value": ""}
