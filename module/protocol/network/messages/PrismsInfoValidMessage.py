from module.protocol.network.message import Message


class PrismsInfoVal5377(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5377
        self.fights = {"type": "Vector.<PrismFightersInformation>", "value": ""}
