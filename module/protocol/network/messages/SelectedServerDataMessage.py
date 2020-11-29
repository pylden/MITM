from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SelectedServerDataMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6182
        self.vars.append({"name": "serverId", "type": "uint", "value": ""})
        self.vars.append({"name": "address", "type": "String", "value": ""})
        self.vars.append({"name": "ports", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "canCreateNewCharacter", "type": "Boolean", "value": ""})
        self.vars.append({"name": "ticket", "type": "Vector.<int>", "value": ""})
