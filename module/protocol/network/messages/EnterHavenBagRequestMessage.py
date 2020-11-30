from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EnterHavenBagRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2716
        self.havenBagOwner = {"type": "Number", "value": ""}
