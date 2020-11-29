from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SubscriptionZoneMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9729
        self.vars.append({"name": "active", "type": "Boolean", "value": ""})
