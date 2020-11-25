from module.protocol.network.message import Message


class PartyUpdateLightMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8915
        self.id = {"type": "Number", "value": ""}
        self.lifePoints = {"type": "uint", "value": ""}
        self.maxLifePoints = {"type": "uint", "value": ""}
        self.prospecting = {"type": "uint", "value": ""}
        self.regenRate = {"type": "uint", "value": ""}
