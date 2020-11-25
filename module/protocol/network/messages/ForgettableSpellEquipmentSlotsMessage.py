from module.protocol.network.message import Message


class ForgettableSpellEquipmentSlotsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 600
        self.quantity = {"type": "int", "value": ""}
