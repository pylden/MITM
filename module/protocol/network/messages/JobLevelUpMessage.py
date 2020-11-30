from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobLevelUpMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2124
        self.newLevel = {"type": "uint", "value": ""}
        self.jobsDescription = {"type": "JobDescription", "value": ""}
