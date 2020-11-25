from module.protocol.network.message import Message


class TaxCollectorDialogQuestionExtendedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5380
        self.maxPods = {"type": "uint", "value": ""}
        self.prospecting = {"type": "uint", "value": ""}
        self.wisdom = {"type": "uint", "value": ""}
        self.taxCollectorsCount = {"type": "uint", "value": ""}
        self.taxCollectorAttack = {"type": "int", "value": ""}
        self.kamas = {"type": "Number", "value": ""}
        self.experience = {"type": "Number", "value": ""}
        self.pods = {"type": "uint", "value": ""}
        self.itemsValue = {"type": "Number", "value": ""}
