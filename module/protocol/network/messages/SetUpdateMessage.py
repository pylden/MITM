from module.protocol.network.message import Message


class SetUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1745
        self.setId = {"type": "uint", "value": ""}
        self.setObjects = {"type": "Vector.<uint>", "value": ""}
        self.setEffects = {"type": "Vector.<ObjectEffect>", "value": ""}
