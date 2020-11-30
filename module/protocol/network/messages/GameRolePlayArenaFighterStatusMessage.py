from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaFighterStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7701
        self.fightId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.accepted = {"type": "Boolean", "value": ""}
