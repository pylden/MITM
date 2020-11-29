from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceCreationResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7888
        self.vars.append({"name": "result", "type": "uint", "value": ""})
