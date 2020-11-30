from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5355
        self.fightId = {"type": "uint", "value": ""}
        self.alliesId = {"type": "Vector.<Number>", "value": ""}
        self.duration = {"type": "uint", "value": ""}
