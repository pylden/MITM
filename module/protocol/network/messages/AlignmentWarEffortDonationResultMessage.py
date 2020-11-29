from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonationResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6877
        self.vars.append({"name": "result", "type": "int", "value": ""})
