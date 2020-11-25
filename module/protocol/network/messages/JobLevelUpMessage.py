from module.protocol.network.message import Message


class JobLevelUpMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2124
        self.newLevel = {"type": "uint", "value": ""}
        self.jobsDescription = {"type": "JobDescription", "value": ""}
