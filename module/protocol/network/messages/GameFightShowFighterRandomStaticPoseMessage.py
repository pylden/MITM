from module.protocol.network.messages.GameFightShowFighterMessage import GameFightShowFighterMessage


class GameFightShowFighterRandomStaticPoseMessage(GameFightShowFighterMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightShowFighterMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2765
