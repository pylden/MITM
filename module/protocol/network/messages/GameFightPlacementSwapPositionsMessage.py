from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4901
        self.vars.append({"name": "dispositions", "type": "Vector.<IdentifiedEntityDispositionInformations>", "value": ""})
