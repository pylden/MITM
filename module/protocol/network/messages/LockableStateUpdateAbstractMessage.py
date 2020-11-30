from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LockableStateUpdateAbstractMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4237
        self.locked = {"type": "Boolean", "value": ""}
