from module.protocol.network.message import Message


class PrismsInfoValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5377
        self.fights = {"type": "Vector.<PrismFightersInformation>", "value": ""}
