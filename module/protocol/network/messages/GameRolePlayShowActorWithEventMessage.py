from module.protocol.network.messages.GameRolePlayShowActorMessage import GameRolePlayShowActorMessage


class GameRolePlayShowActorWithEventMessage(GameRolePlayShowActorMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameRolePlayShowActorMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1817
        self.actorEventId = {"type": "uint", "value": ""}
