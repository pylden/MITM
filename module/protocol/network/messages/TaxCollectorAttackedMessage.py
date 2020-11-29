from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorAttackedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4380
        self.vars.append({"name": "firstNameId", "type": "uint", "value": ""})
        self.vars.append({"name": "lastNameId", "type": "uint", "value": ""})
        self.vars.append({"name": "worldX", "type": "int", "value": ""})
        self.vars.append({"name": "worldY", "type": "int", "value": ""})
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "guild", "type": "BasicGuildInformations", "value": ""})
