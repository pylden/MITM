from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportDestinationsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1851
        self.type = {"type": "uint", "value": ""}
        self.destinations = {"type": "Vector.<TeleportDestination>", "value": ""}
