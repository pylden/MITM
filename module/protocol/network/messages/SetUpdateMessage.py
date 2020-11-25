from module.protocol.network.message import Message


class SetUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1745
        self.setId = {"type": "uint", "value": ""}
        self.setObjects = {"type": "Vector.<uint>", "value": ""}
        self.setEffects = {"type": "Vector.<ObjectEffect>", "value": ""}
