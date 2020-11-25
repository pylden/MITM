from module.protocol.network.message import Message


class CharacterExperienceGainMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9931
        self.experienceCharacter = {"type": "Number", "value": ""}
        self.experienceMount = {"type": "Number", "value": ""}
        self.experienceGuild = {"type": "Number", "value": ""}
        self.experienceIncarnation = {"type": "Number", "value": ""}
