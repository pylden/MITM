from module.protocol.network.message import Message


class BasicStatWithDataMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5159
        self.datas = {"type": "Vector.<StatisticData>", "value": ""}
