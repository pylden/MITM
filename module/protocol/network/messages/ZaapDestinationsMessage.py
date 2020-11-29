from module.protocol.network.messages.TeleportDestinationsMessage import TeleportDestinationsMessage


class ZaapDestinationsMessage(TeleportDestinationsMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        TeleportDestinationsMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7339
        self.vars.append({"name": "spawnMapId", "type": "Number", "value": ""})
