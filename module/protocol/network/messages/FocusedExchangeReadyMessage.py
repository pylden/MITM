from module.protocol.network.messages.ExchangeReadyMessage import ExchangeReadyMessage


class FocusedExchangeReadyMessage(ExchangeReadyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeReadyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9510
        self.focusActionId = {"type": "uint", "value": ""}
