from module.protocol.network.utils.boolean_byte_wrapper import BooleanByteWrapper

class GameServerInformations:
    protocolId = 5868

    def __init__(self):
        self.id = 0
        self.type = -1
        self.is_mono_account = False
        self.status = 1
        self.completion = 0
        self.is_selectable = False
        self.characters_count = 0
        self.characters_slots = 0
        self.date = 0

    def deserialize(self, buffer):
        box = int.from_bytes(buffer.read_char(), 'big')
        self.is_mono_account = BooleanByteWrapper.get_flag(box, 0)
        self.is_selectable = BooleanByteWrapper.get_flag(box, 1)
        self.id = buffer.read_read_var_uh_short()
        self.type = buffer.read_char()
        self.status = buffer.read_char()
        self.completion = buffer.read_char()
        self.characters_count = buffer.read_char()
        self.characters_slots = buffer.read_char()
        self.date = buffer.read_double()


    def __repr__(self):
        return "IsMonoAccount: {0}, IsSelectable: {1}, ID: {2}, Type: {3}, Status: {4}, Completion: {5}, CC: {6}, CS: {7}, Date: {8}".format(
            self.is_mono_account,
            self.is_selectable,
            self.id,
            self.type,
            self.status,
            self.completion,
            self.characters_count,
            self.characters_slots,
            self.date
        )
