from module.protocol.network.messages.GameRolePlayDelayedActionMessage import GameRolePlayDelayedActionMessage


class GameRolePlayDelayedObjectUseMessage(GameRolePlayDelayedActionMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameRolePlayDelayedActionMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1711
        self.objectGID = {"type": "uint", "value": ""}
