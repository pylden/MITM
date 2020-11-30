from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFightPlayersHelpersLeaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2966
        self.fightId = {"type": "Number", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
