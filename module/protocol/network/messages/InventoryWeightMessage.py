from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InventoryWeightMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1306
        self.vars.append({"name": "inventoryWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "shopWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "weightMax", "type": "uint", "value": ""})
