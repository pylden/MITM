from module.protocol.network.message import Message


class MapComplementaryInformationsDataInHavenBagMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3465
        self.ownerInformations = {"type": "CharacterMinimalInformations", "value": ""}
        self.theme = {"type": "int", "value": ""}
        self.roomId = {"type": "uint", "value": ""}
        self.maxRoomId = {"type": "uint", "value": ""}
