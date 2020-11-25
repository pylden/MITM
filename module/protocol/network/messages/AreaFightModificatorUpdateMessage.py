from module.protocol.network.message import Message


class AreaFightModificatorUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4723
        self.spellPairId = {"type": "int", "value": ""}
