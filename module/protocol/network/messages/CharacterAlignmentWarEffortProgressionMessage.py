from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CharacterAlignmentWarEffortProgressionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2972
        self.vars.append({"name": "alignmentWarEffortDailyLimit", "type": "Number", "value": ""})
        self.vars.append({"name": "alignmentWarEffortDailyDonation", "type": "Number", "value": ""})
        self.vars.append({"name": "alignmentWarEffortPersonalDonation", "type": "Number", "value": ""})
