from DEF import *
from Tables import *

class DES_structure:

    Def = DEF()

    def key_generation(self, Key):
        Key_after_initial_permut = self.Def.permut(Tables.PC_1, Key)

        (C0, D0) = self.Def.divide_X(Key_after_initial_permut)

        Key0 = self.Def.permut(Tables.PC_2, self.Def.merg(C0, D0))
        print('Key0 = ' + self.Def.bin2hexa(Key0))

        #generate other keys
        C = C0; D = D0
        Keys = []

        for i in range(0, 16):
            C = self.Def.shift(C, Tables.SHIFT[i])
            D = self.Def.shift(D, Tables.SHIFT[i])
            key = self.Def.merg(C, D)

            key_after_final_permut = self.Def.permut(Tables.PC_2, key)
            Keys.append(key_after_final_permut)
            key_name = ('Key' + str(i + 1))
            print(key_name + ' = ' + self.Def.bin2hexa(key_after_final_permut))

        return Keys




    def encryption(self, Plain, Key):
        Keys = self.key_generation(Key)

        Plain_after_initial_permut = self.Def.permut(Tables.IP, Plain)
        (L0, R0) = self.Def.divide_X(Plain_after_initial_permut)
        print('L0 = ' + self.Def.bin2hexa(L0))
        print('R0 = ' + self.Def.bin2hexa(R0))


        l = L0; r = R0
        for i in range(0, 16):
            (l, r) = self.Def.generate_rounds_encryption(l, r, Keys[i])
            round_left_name = ('L' + str(i + 1))
            round_right_name = ('R' + str(i + 1))
            print(round_left_name + ' = ' + self.Def.bin2hexa(l))
            print(round_right_name + ' = ' + self.Def.bin2hexa(r))


        (L, R) = self.Def.swaping(l, r)

        LR = self.Def.merg(L, R)

        IP_1 = self.Def.permut(Tables.IP_INVERSE, LR)

        Cipher = self.Def.bin2hexa(IP_1)
        print('-------------------------------------------')
        print('Cipher text is : ' + Cipher)

        return Cipher




    def decryption(self, Cipher, Key):
        Keys = self.key_generation(Key)

        Cipher_after_initial_permut = self.Def.permut(Tables.IP, Cipher)
        (L16_, R16_) = self.Def.divide_X(Cipher_after_initial_permut)
        (L16, R16) = self.Def.swaping(L16_, R16_)
        print('L16 = ' + self.Def.bin2hexa(L16))
        print('R16 = ' + self.Def.bin2hexa(R16))


        l = L16; r = R16
        i = 15
        while i >= 0:
            (l, r) = self.Def.generate_rounds_decryption(l, r, Keys[i])
            round_left_name = ('L' + str(i))
            round_right_name = ('R' + str(i))
            print(round_left_name + ' = ' + self.Def.bin2hexa(l))
            print(round_right_name + ' = ' + self.Def.bin2hexa(r))
            i -= 1


        LR = self.Def.merg(l, r)

        IP_1 = self.Def.permut(Tables.IP_INVERSE, LR)

        Plain = self.Def.bin2hexa(IP_1)
        print('-------------------------------------------')
        print('Plain text is : ' + Plain)

        return Plain