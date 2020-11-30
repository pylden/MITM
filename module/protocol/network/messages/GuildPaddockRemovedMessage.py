from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildPaddockRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6712
        self.paddockId = {"type": "Number", "value": ""}
