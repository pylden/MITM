from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterDeletionRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5853
        self.characterId = {"type": "Number", "value": ""}
        self.secretAnswerHash = {"type": "String", "value": ""}
