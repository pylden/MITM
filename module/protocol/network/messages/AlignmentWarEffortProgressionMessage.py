from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortProgressionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5772
        self.vars.append({"name": "effortProgressions", "type": "Vector.<AlignmentWarEffortInformation>", "value": ""})
