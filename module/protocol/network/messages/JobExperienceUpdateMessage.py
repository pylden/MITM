from module.protocol.network.message import Message


class JobExperienceUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2969
        self.experiencesUpdate = {"type": "JobExperience", "value": ""}
