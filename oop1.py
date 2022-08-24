class Mobil:
    merk = "toyota"
    def isibbm(self,a):
        return (f'isi bbmnya = {str(a)}')

class Mvp(Mobil):
    #pass
    __harga = 150
    def jmlpenumpang(self,a):
        if a == 'panjang':
            return ('jumlah penumpang = 8')
        else :
            return ('jumlah penumpang = 5')

    def hargasecond(self,type):
        if type == 'hiace':
            return (self.__harga) 
        else :
            return ('tidak tahu')

    @classmethod
    def testclassmethod(cls):
        return ('ini class method')

if __name__ == '__main__':
    avanza = Mvp()
    print(avanza.merk) 
    print(avanza.isibbm(10))
    print(avanza.jmlpenumpang('panjang'))
    print(avanza.testclassmethod())
    print(avanza.jmlpenumpang('pendek'))