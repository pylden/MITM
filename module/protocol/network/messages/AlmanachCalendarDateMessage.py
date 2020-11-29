from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AlmanachCalendarDateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8154
        self.vars.append({"name": "date", "type": "int", "value": ""})
