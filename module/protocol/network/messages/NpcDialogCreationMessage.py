from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NpcDialogCreationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6950
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
        self.vars.append({"name": "npcId", "type": "int", "value": ""})
