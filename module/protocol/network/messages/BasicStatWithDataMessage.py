from module.protocol.network.messages.BasicStatMessage import BasicStatMessage


class BasicStatWithDataMessage(BasicStatMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        BasicStatMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5159
        self.datas = {"type": "Vector.<StatisticData>", "value": ""}
