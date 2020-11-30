from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8697
        self.ignoredList = {"type": "Vector.<IgnoredInformations>", "value": ""}
