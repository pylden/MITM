from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DisplayNumericalValuePaddockMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5107
        self.rideId = {"type": "int", "value": ""}
        self.value = {"type": "int", "value": ""}
        self.type = {"type": "uint", "value": ""}
