from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonatePreviewMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3338
        self.xp = {"type": "Number", "value": ""}
