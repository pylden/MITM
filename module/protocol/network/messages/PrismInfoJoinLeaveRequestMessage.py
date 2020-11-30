from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismInfoJoinLeaveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 997
        self.join = {"type": "Boolean", "value": ""}
