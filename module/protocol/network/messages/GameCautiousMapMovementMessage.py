from module.protocol.network.messages.GameMapMovementMessage import GameMapMovementMessage


class GameCautiousMapMovementMessage(GameMapMovementMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameMapMovementMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3587
