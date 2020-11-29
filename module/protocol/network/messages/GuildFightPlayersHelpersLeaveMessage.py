from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFightPlayersHelpersLeaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2966
        self.vars.append({"name": "fightId", "type": "Number", "value": ""})
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
