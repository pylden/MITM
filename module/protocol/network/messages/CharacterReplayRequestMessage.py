from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterReplayRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1391
        self.vars.append({"name": "characterId", "type": "Number", "value": ""})
