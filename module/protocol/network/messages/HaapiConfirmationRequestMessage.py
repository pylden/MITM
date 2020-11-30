from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiConfirmationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3477
        self.kamas = {"type": "Number", "value": ""}
        self.ogrines = {"type": "Number", "value": ""}
        self.rate = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
