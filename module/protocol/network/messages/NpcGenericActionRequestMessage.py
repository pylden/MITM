from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NpcGenericActionRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3595
        self.vars.append({"name": "npcId", "type": "int", "value": ""})
        self.vars.append({"name": "npcActionId", "type": "uint", "value": ""})
        self.vars.append({"name": "npcMapId", "type": "Number", "value": ""})
