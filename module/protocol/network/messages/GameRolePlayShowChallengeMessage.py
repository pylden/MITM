from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayShowChallengeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5095
        self.commonsInfos = {"type": "FightCommonInformations", "value": ""}
