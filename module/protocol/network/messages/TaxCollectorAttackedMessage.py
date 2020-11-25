from module.protocol.network.message import Message


class TaxCollectorAttackedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4380
        self.firstNameId = {"type": "uint", "value": ""}
        self.lastNameId = {"type": "uint", "value": ""}
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
        self.subAreaId = {"type": "uint", "value": ""}
        self.guild = {"type": "BasicGuildInformations", "value": ""}
