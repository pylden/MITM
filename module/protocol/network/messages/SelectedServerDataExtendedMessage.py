from module.protocol.network.messages.SelectedServerDataMessage import SelectedServerDataMessage


class SelectedServerDataExtendedMessage(SelectedServerDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        SelectedServerDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8204
        self.vars.append({"name": "servers", "type": "Vector.<GameServerInformations>", "value": ""})
