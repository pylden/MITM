from module.protocol.network.messages.NetworkMessage import NetworkMessage


class UpdateSelfAgressableStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1451
        self.status = {"type": "uint", "value": ""}
        self.probationTime = {"type": "uint", "value": ""}
