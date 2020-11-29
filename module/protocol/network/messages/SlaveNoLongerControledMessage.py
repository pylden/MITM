from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SlaveNoLongerControledMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8594
        self.vars.append({"name": "masterId", "type": "Number", "value": ""})
        self.vars.append({"name": "slaveId", "type": "Number", "value": ""})
