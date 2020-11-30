from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9931
        self.experienceCharacter = {"type": "Number", "value": ""}
        self.experienceMount = {"type": "Number", "value": ""}
        self.experienceGuild = {"type": "Number", "value": ""}
        self.experienceIncarnation = {"type": "Number", "value": ""}
