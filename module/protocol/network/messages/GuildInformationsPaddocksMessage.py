from module.protocol.network.message import Message


class GuildInformationsPaddocksMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6791
        self.nbPaddockMax = {"type": "uint", "value": ""}
        self.paddocksInformations = {"type": "Vector.<PaddockContentInformations>", "value": ""}
