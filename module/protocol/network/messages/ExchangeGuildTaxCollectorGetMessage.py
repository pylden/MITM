from module.protocol.network.message import Message


class ExchangeGuildTaxCollectorGetMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2767
        self.collectorName = {"type": "String", "value": ""}
        self.userName = {"type": "String", "value": ""}
        self.callerName = {"type": "String", "value": ""}
