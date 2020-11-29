from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterExperienceGainMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9931
        self.vars.append({"name": "experienceCharacter", "type": "Number", "value": ""})
        self.vars.append({"name": "experienceMount", "type": "Number", "value": ""})
        self.vars.append({"name": "experienceGuild", "type": "Number", "value": ""})
        self.vars.append({"name": "experienceIncarnation", "type": "Number", "value": ""})
