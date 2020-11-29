from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DisplayNumericalValuePaddockMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5107
        self.vars.append({"name": "rideId", "type": "int", "value": ""})
        self.vars.append({"name": "value", "type": "int", "value": ""})
        self.vars.append({"name": "type", "type": "uint", "value": ""})
