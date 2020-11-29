from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InteractiveUsedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9839
        self.vars.append({"name": "entityId", "type": "Number", "value": ""})
        self.vars.append({"name": "elemId", "type": "uint", "value": ""})
        self.vars.append({"name": "skillId", "type": "uint", "value": ""})
        self.vars.append({"name": "duration", "type": "uint", "value": ""})
        self.vars.append({"name": "canMove", "type": "Boolean", "value": ""})
