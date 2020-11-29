from module.protocol.network.messages.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage


class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeStartOkMountWithOutPaddockMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1272
        self.vars.append({"name": "paddockedMountsDescription", "type": "Vector.<MountClientData>", "value": ""})
