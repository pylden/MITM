from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SequenceEndMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8673
        self.vars.append({"name": "actionId", "type": "uint", "value": ""})
        self.vars.append({"name": "authorId", "type": "Number", "value": ""})
        self.vars.append({"name": "sequenceType", "type": "int", "value": ""})
