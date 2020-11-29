from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobBookSubscriptionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9091
        self.vars.append({"name": "subscriptions", "type": "Vector.<JobBookSubscription>", "value": ""})
