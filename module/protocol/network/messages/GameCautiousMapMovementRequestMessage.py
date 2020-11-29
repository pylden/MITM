from module.protocol.network.messages.GameMapMovementRequestMessage import GameMapMovementRequestMessage


class GameCautiousMapMovementRequestMessage(GameMapMovementRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameMapMovementRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 189
