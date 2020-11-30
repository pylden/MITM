from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkJobIndexMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 342
        self.jobs = {"type": "Vector.<uint>", "value": ""}
