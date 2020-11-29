from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobLevelUpMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2124
        self.vars.append({"name": "newLevel", "type": "uint", "value": ""})
        self.vars.append({"name": "jobsDescription", "type": "JobDescription", "value": ""})
