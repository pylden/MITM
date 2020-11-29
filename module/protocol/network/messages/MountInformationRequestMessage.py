from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountInformationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5729
        self.vars.append({"name": "id", "type": "Number", "value": ""})
        self.vars.append({"name": "time", "type": "Number", "value": ""})
