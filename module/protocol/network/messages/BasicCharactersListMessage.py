from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicCharactersListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3322
        self.vars.append({"name": "characters", "type": "Vector.<CharacterBaseInformations>", "value": ""})
