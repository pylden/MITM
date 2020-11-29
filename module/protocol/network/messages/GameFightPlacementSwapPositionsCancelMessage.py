from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 533
        self.vars.append({"name": "requestId", "type": "uint", "value": ""})
