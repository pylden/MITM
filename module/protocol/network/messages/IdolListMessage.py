from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9934
        self.chosenIdols = {"type": "Vector.<uint>", "value": ""}
        self.partyChosenIdols = {"type": "Vector.<uint>", "value": ""}
        self.partyIdols = {"type": "Vector.<PartyIdol>", "value": ""}
