from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayShowActorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9281
        self.vars.append({"name": "informations", "type": "GameRolePlayActorInformations", "value": ""})
