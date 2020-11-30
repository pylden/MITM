from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SystemMessageDisplayMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4995
        self.hangUp = {"type": "Boolean", "value": ""}
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
