from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonateRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5455
        self.vars.append({"name": "donation", "type": "Number", "value": ""})
