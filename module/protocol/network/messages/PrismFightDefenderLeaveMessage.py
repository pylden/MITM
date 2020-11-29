from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightDefenderLeaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9060
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "fighterToRemoveId", "type": "Number", "value": ""})
