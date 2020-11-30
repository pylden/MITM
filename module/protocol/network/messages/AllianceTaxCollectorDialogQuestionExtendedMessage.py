from module.protocol.network.messages.TaxCollectorDialogQuestionExtendedMessage import TaxCollectorDialogQuestionExtendedMessage


class AllianceTaxCollectorDialogQuestionExtendedMessage(TaxCollectorDialogQuestionExtendedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        TaxCollectorDialogQuestionExtendedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 164
        self.alliance = {"type": "BasicNamedAllianceInformations", "value": ""}
