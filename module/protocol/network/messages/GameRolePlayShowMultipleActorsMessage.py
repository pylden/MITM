from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayShowMultipleActorsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4416
        self.informationsList = {"type": "Vector.<GameRolePlayActorInformations>", "value": ""}
