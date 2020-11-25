from module.protocol.network.message import Message


class HavenBagFurnituresMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 709
        self.furnituresInfos = {"type": "Vector.<HavenBagFurnitureInformation>", "value": ""}
