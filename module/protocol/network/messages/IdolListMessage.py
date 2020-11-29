from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9934
        self.vars.append({"name": "chosenIdols", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "partyChosenIdols", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "partyIdols", "type": "Vector.<PartyIdol>", "value": ""})
