from module.protocol.network.messages.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage


class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightPlacementPositionRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9517
        self.requestedId = {"type": "Number", "value": ""}
