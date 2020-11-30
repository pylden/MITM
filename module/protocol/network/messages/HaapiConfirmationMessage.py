from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7797
        self.kamas = {"type": "Number", "value": ""}
        self.amount = {"type": "Number", "value": ""}
        self.rate = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
        self.transaction = {"type": "String", "value": ""}
