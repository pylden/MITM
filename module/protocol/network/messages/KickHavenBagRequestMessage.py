from module.protocol.network.messages.NetworkMessage import NetworkMessage


class KickHavenBagRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 711
        self.guestId = {"type": "Number", "value": ""}
