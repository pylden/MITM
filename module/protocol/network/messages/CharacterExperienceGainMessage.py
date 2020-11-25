from module.protocol.network.message import Message


class CharacterExperienceGainMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9931
        self.experienceCharacter = {"type": "Number", "value": ""}
        self.experienceMount = {"type": "Number", "value": ""}
        self.experienceGuild = {"type": "Number", "value": ""}
        self.experienceIncarnation = {"type": "Number", "value": ""}
