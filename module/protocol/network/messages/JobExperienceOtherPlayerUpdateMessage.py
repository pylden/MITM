from module.protocol.network.messages.JobExperienceUpdateMessage import JobExperienceUpdateMessage


class JobExperienceOtherPlayerUpdateMessage(JobExperienceUpdateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        JobExperienceUpdateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7414
        self.playerId = {"type": "Number", "value": ""}
