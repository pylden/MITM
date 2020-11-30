from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7685
        self.subAreaId = {"type": "uint", "value": ""}
        self.join = {"type": "Boolean", "value": ""}
