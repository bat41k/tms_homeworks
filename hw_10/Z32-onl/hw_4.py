alphabet_dec = 'A B C D E F G H I  J  K L M N O P Q R S T U V W X Y Z'.replace(' ', '')
alphabet_enc = 'C R Y P T O A B D E F G H  I  J  K L M N Q S U V W X Z'.replace(' ', '')

alphabet_dec = alphabet_dec + alphabet_dec.lower()
alphabet_enc = alphabet_enc + alphabet_enc.lower()


class Cipher:

    @staticmethod
    def encode(keywords: str) -> None:
        print(keywords.translate(str.maketrans(alphabet_dec, alphabet_enc)))

    @staticmethod
    def decode(keywords: str) -> None:
        print(keywords.translate(str.maketrans(alphabet_enc, alphabet_dec)))


cipher = Cipher()

cipher.encode('Hello, world')
cipher.decode('Fjedhc dn atidsn')