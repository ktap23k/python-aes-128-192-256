import aes

class CHOOSE:
    """
    Chọn loại mã hoá
    """
    def __init__(self, mode_master, key, inp , iv):
        self.mode = mode_master
        self.key = key
        self.inp = inp
        self.iv = iv
        self._createAES()

    def _createAES(self):
        self.crypt = aes.AES(self.key)

    def Encrypt(self):
        if self.mode=='AES':
            return self.crypt.encrypt(self.inp)
        elif self.mode=='AES_CBC':
            return self.crypt.encrypt_cbc(self.inp,self.iv)
        elif self.mode=='AES_PCBC':
            return self.crypt.encrypt_pcbc(self.inp, self.iv)
        elif self.mode=='AES_CFB':
            return self.crypt.encrypt_cfb(self.inp, self.iv)
        elif self.mode=='AES_OFB':
            return self.crypt.encrypt_ofb(self.inp, self.iv)
        elif self.mode=='AES_CTR':
            return self.crypt.encrypt_ctr(self.inp, self.iv)

    def Decrypt(self):
        if self.mode=='AES':
            return self.crypt.decrypt(self.inp)
        elif self.mode=='AES_CBC':
            return self.crypt.decrypt_cbc(self.inp,self.iv)
        elif self.mode=='AES_PCBC':
            return self.crypt.decrypt_pcbc(self.inp, self.iv)
        elif self.mode=='AES_CFB':
            return self.crypt.decrypt_cfb(self.inp, self.iv)
        elif self.mode=='AES_OFB':
            return self.crypt.decrypt_ofb(self.inp, self.iv)
        elif self.mode=='AES_CTR':
            return self.crypt.decrypt_ctr(self.inp, self.iv)