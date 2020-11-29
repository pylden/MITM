from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachTeleportResponseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 870
        self.vars.append({"name": "teleported", "type": "Boolean", "value": ""})
