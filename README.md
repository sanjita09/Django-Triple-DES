# Django-Triple-DES
A simple web page that compresses images using TRIPLE DES ALGORITHM

The Triple DES algorithm uses three iterations of the common DES cipher. It receives a secret 168-bit key, which is divided into three 64-bit keys. The least significant 
(right-most) bit in each byte is a parity bit, and should be set so that there are always an odd number of 1s in every byte. These parity bits are ignored, so only the seven
most significant bits of each byte are used, resulting in a key length of 56 bits. This means that the effective key strength for Triple DES is actually 168 bits because each 
of the three keys contains 8 parity bits that are not used during the encryption process.
   
    • Encryption using the first secret key
    • Decryption using the second secret key
    • Encryption using the third secret key

Encryption: c = E3 (D2 (E1 (m)))
Decryption: m = D1 (E2 (D3(c)))
