from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachRoomUnlockResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7688
        self.vars.append({"name": "roomId", "type": "uint", "value": ""})
        self.vars.append({"name": "result", "type": "uint", "value": ""})
