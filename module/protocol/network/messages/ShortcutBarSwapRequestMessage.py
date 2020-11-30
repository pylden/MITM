from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShortcutBarSwapRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6397
        self.barType = {"type": "uint", "value": ""}
        self.firstSlot = {"type": "uint", "value": ""}
        self.secondSlot = {"type": "uint", "value": ""}
