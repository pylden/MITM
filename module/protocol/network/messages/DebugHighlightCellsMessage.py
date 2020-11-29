from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DebugHighlightCellsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1636
        self.vars.append({"name": "color", "type": "Number", "value": ""})
        self.vars.append({"name": "cells", "type": "Vector.<uint>", "value": ""})
