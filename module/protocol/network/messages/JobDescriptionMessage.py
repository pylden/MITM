from module.protocol.network.messages.NetworkMessage import NetworkMessage


class JobDescriptionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 414
        self.vars.append({"name": "jobsDescription", "type": "Vector.<JobDescription>", "value": ""})
