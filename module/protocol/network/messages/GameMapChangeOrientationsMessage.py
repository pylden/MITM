from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameMapChangeOrientationsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1921
        self.orientations = {"type": "Vector.<ActorOrientation>", "value": ""}
