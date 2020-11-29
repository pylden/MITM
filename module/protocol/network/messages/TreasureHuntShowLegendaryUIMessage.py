from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntShowLegendaryUIMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 207
        self.vars.append({"name": "availableLegendaryIds", "type": "Vector.<uint>", "value": ""})
