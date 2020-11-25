from module.protocol.network.message import Message


class PartyUpdateLightMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8915
        self.id = {"type": "Number", "value": ""}
        self.lifePoints = {"type": "uint", "value": ""}
        self.maxLifePoints = {"type": "uint", "value": ""}
        self.prospecting = {"type": "uint", "value": ""}
        self.regenRate = {"type": "uint", "value": ""}
