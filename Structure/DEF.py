from Tables.Tables import *

class DEF:


    def shift(self, x, n):

        return x[n:] + x[:n]


    def permut(self, table, X):
        X_after_permut = ''
        for i in table:
            X_after_permut += X[i - 1]

        return X_after_permut


    def divide_X(self, x):
        size = len(x)
        center_divide = int(size / 2)
        C = x[:center_divide]
        D = x[center_divide:]

        return (C, D)


    def xor(self, X, Y):
        n = len(X)
        result = ''
        for i in range(0, n):
            if X[i] != Y[i]:
                result += '1'
            elif X[i] == Y[i]:
                result += '0'

        return result


    def s_box(self, result_after_xor):
        result_after_sbox = ''
        for i in range(0, 48, 6):
            block = result_after_xor[i:i + 6]
            s_box = Tables.S_BOXES[i]
            column_In_Binary = block[1:-1]
            row_In_Binary = self.merg(block[0], block[5])
            column_In_Decimal = self.bin2dec(column_In_Binary)
            row_In_Decimal = self.bin2dec(row_In_Binary)
            result_sbox_block_decimal = s_box[row_In_Decimal][column_In_Decimal]
            result_sbox_block_binary = self.dec2bin(result_sbox_block_decimal, 4)
            result_after_sbox += result_sbox_block_binary

        return result_after_sbox


    def mangler_function(self, R, key_of_round):
        expansion = self.permut(Tables.E_D_BOX, R)
        result_after_xor = self.xor(expansion, key_of_round)
        # s_box
        result_after_sbox = self.s_box(result_after_xor)
        result_after_straightDBox = self.permut(Tables.STRAIGHT_D_BOX, result_after_sbox)

        return result_after_straightDBox


    def generate_rounds_encryption(self, L, R, key_of_round):
        l = R
        MF = self.mangler_function(R, key_of_round)
        r = self.xor(MF, L)

        return (l, r)


    def generate_rounds_decryption(self, L, R, key_of_round):
        r = L
        MF = self.mangler_function(r, key_of_round)
        l = self.xor(MF, R)

        return (l, r)


    def swaping(self, l, r):
        l, r = r, l

        return (l, r)


    def merg(self, x, y):

        return x + y


    def check(self, X):
        if len(X) < 16:
            lost_len = 16 - len(X)
            for i in range(0, lost_len):
                X = X + '0'

        return X


    def is_hexa(self, X):
        hexa_digits = '0123456789abcdefABCDEF'
        for i in X:
            if i not in hexa_digits:

                return False

        return True


    def bin2dec(self, x):

        return int(x, 2)


    def hexa2dec(self, x):

        return int(x, 16)


    def bin2hexa(self, x):
        n = int(len(x)/4)

        return hex(self.bin2dec(x))[2:].zfill(n)


    def dec2bin (self, x, n):

        return format(x, 'b').zfill(n)


    def hexa2bin(self, x):
        n = int(len(x) * 4)

        return self.dec2bin(self.hexa2dec(x), n)
