
# RSA-Encryption

This projects demonstates the RSA encryption algorithm on python.

### Working.

1. Prime Generation generates two prime numbers along with the secret key N. This N = p*q <br />
PrimeGeneration: Input: --🦖 || Output: p,q,n <br /><br />
2. This p,q is now passed through find_d python script which will find f(p,q) = z which is used to generate two keys e and d respectively. <br />
find_d: Input(Change inside the file): p,q || Outputs (f(p,q) \n 1 \n (d,e)<br /><br />
3. Encryptor These is a package containing all encrypting and decrypting functions. We have to feed all input variables that we have generated till now. This will generate encrypted text using two ASCII character and connected in ECB (Electronic Code block) with a block size of 2 ASCII character. Two block concatenation is used because single ASCII block is prone to frequency attacks. <br />
Encryptor: INPUT(Change inside the file):p,q,e,d || OUTPUT: --🦖 <br /><br />
4. Version1 is single block ECB encryption <br />
Version1: Input : mode Input_file output_file<br />

5. Version2 is two concatenation block ECB encryption <br />
Version2: Input : mode Input_file output_file<br />

#### Requirements

- Python3

#### How to run:

Open terminal in current location<br />

To generate new keys<br />
```
  python PrimeGeneration.py
```
Take these numbers and put *p,q* into **_find_d.py_** <br />
```
  python find_d.py
```
Now you have generated all the keys. Save these keys into **_Encryptor.py_**

To encrypt file (encryptedFile will be generated in the same folder. If same file exists it will be overwritten)
```
  python Version1.py 0 <PlainText.txt> <encryptedFile.Txt>
```
Use this for concatenation ECB Encryption
```   
  python Version2.py 0 <PlainText.txt> <encryptedFile.Txt>
```
To Decrypt file 
```
  python Version1.py 1 <encryptedFile.txt>
```  
 Use this for concatenation ECB Decryption
```  
  python Version2.py 1 <PlainText.txt> <encryptedFile.Txt>
```

