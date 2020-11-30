class BooleanByteWrapper:
    def get_flag(a, pos):
        if pos == 0:
            return (a & 1) != 0;
        if pos ==1:
            return (a & 2) != 0;
        if pos == 2:
            return (a & 4) != 0;
        if pos == 3:
            return (a & 8) != 0;
        if pos == 4:
            return (a & 16) != 0;
        if pos == 5:
            return (a & 32) != 0;
        if pos == 6:
            return (a & 64) != 0;
        if pos == 7:
            return (a & 128) != 0;
        raise Exception('Bytebox overflow.')

    get_flag = staticmethod(get_flag)
