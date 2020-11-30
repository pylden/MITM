from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ContactLookRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4354
        self.requestId = {"type": "uint", "value": ""}
        self.contactType = {"type": "uint", "value": ""}
