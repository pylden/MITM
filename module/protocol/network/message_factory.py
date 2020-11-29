from module.io.BytesReader import BytesReader
from module.protocol.network.messages_dict import MessagesDict


class MessageFactory:
    def message(buffer, from_client=False):
        buffer_reader = BytesReader(buffer)
        print(buffer_reader.get_current_buffer().hex())

        if len(buffer) < 8:  # If the current buffer is not even the size of header
            print("Header too small")
            return None

        print("From client %d" % from_client)
        hi_header = buffer_reader.read(2)
        count = None if not from_client else buffer_reader.read_uint()[0]
        id = int.from_bytes(hi_header, 'big') >> 2
        len_type = int.from_bytes(hi_header, 'big') & 3
        length = int.from_bytes(buffer_reader.read(len_type), 'big')
        print("Id => {0}\nlen_type => {1}\nlen => {2}\ncount => {3}".format(id, len_type, length, count))

        if buffer_reader.get_current_buffer().nbytes < length:  # If the current buffer is small than the packet length.
            print("Packet too small")
            return None

        msg = buffer_reader.read(length)

        try:
            msg = MessagesDict[id](BytesReader(msg), len_type, length, count=count)
            msg.deserialize()
            return msg
        except KeyError:
            print("ID not found: %d" % id)
            exit()

    message = staticmethod(message)
