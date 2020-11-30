from module.protocol.network.messages.CurrentMapMessage import CurrentMapMessage


class CurrentMapInstanceMessage(CurrentMapMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CurrentMapMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4034
        self.instantiatedMapId = {"type": "Number", "value": ""}
