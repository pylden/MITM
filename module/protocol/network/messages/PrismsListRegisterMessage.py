from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismsListRegisterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9690
        self.listen = {"type": "uint", "value": ""}
