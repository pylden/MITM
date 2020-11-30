from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorAttackedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4380
        self.firstNameId = {"type": "uint", "value": ""}
        self.lastNameId = {"type": "uint", "value": ""}
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
        self.mapId = {"type": "Number", "value": ""}
        self.subAreaId = {"type": "uint", "value": ""}
        self.guild = {"type": "BasicGuildInformations", "value": ""}
