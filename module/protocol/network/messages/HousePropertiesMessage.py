from module.protocol.network.message import Message


class HousePropertiesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5861
        self.houseId = {"type": "uint", "value": ""}
        self.doorsOnMap = {"type": "Vector.<uint>", "value": ""}
        self.properties = {"type": "HouseInstanceInformations", "value": ""}
