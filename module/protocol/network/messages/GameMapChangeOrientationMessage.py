from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapChangeOrientationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8450
        self.vars.append({"name": "orientation", "type": "ActorOrientation", "value": ""})
