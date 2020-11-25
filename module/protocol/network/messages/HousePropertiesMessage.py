from module.protocol.network.message import Message


class HousePropertiesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5861
        self.houseId = {"type": "uint", "value": ""}
        self.doorsOnMap = {"type": "Vector.<uint>", "value": ""}
        self.properties = {"type": "HouseInstanceInformations", "value": ""}
