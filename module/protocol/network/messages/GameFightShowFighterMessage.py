from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightShowFighterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9957
        self.vars.append({"name": "informations", "type": "GameFightFighterInformations", "value": ""})
