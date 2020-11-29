from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobExperienceUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2969
        self.vars.append({"name": "experiencesUpdate", "type": "JobExperience", "value": ""})
