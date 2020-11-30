from module.protocol.network.messages.HaapiValidationMessage import HaapiValidationMessage


class HaapiBuyValidationMessage(HaapiValidationMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        HaapiValidationMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7568
        self.amount = {"type": "Number", "value": ""}
        self.email = {"type": "String", "value": ""}
