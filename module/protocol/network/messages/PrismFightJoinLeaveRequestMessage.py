from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7685
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "join", "type": "Boolean", "value": ""})
