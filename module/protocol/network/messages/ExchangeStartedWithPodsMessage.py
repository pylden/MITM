from module.protocol.network.message import Message


class ExchangeStartedWithPodsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4599
        self.firstCharacterId = {"type": "Number", "value": ""}
        self.firstCharacterCurrentWeight = {"type": "uint", "value": ""}
        self.firstCharacterMaxWeight = {"type": "uint", "value": ""}
        self.secondCharacterId = {"type": "Number", "value": ""}
        self.secondCharacterCurrentWeight = {"type": "uint", "value": ""}
        self.secondCharacterMaxWeight = {"type": "uint", "value": ""}
