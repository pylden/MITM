from module.protocol.network.message import Message


class HavenBagFurnituresRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1534
        self.cellIds = {"type": "Vector.<uint>", "value": ""}
        self.funitureIds = {"type": "Vector.<int>", "value": ""}
        self.orientations = {"type": "Vector.<uint>", "value": ""}
