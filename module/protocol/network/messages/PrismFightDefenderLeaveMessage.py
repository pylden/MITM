from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightDefenderLeaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9060
        self.subAreaId = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.fighterToRemoveId = {"type": "Number", "value": ""}
