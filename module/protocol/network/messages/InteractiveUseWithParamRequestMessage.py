from module.protocol.network.messages.InteractiveUseRequestMessage import InteractiveUseRequestMessage


class InteractiveUseWithParamRequestMessage(InteractiveUseRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        InteractiveUseRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4240
        self.id = {"type": "int", "value": ""}
