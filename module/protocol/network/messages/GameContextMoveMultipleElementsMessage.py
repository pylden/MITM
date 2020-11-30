from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameContextMoveMultipleElementsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3748
        self.movements = {"type": "Vector.<EntityMovementInformations>", "value": ""}
