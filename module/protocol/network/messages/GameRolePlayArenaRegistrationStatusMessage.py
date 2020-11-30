from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaRegistrationStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2867
        self.registered = {"type": "Boolean", "value": ""}
        self.step = {"type": "uint", "value": ""}
        self.battleMode = {"type": "uint", "value": ""}
