from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightOptionStateUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4253
        self.fightId = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.option = {"type": "uint", "value": ""}
        self.state = {"type": "Boolean", "value": ""}
