from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AccountLoggingKickedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1881
        self.days = {"type": "uint", "value": ""}
        self.hours = {"type": "uint", "value": ""}
        self.minutes = {"type": "uint", "value": ""}
