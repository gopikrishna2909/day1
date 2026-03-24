from operator import index

alphabets=['a','b', 'c', 'd' ,'e', 'f', 'g' ,'h', 'i','j', 'k', 'l' ,'m' ,'n', 'o', 'p' ,'q' ,'r',
         's' ,'t' ,'u' ,'v','w', 'x', 'y', 'z']
direction = input("Type 'encrypt' to Encrypt and 'decrypt' to Decrypt:\n" )
text = input("Enter the text:\n").lower()
shift = int(input("Enter the shift number:\n"))

def encrypt(original_text, shift_amount):
    #alphabests_index = 0
    encrypted_text = ""
    for i in original_text:
        alphabests_index = alphabets.index(i)+shift
        # if alphabests_index <= 26:
        #     encrypted_text += alphabets[alphabests_index]
        # else:
        #     encrypted_text += alphabets[(alphabets.index(i)+shift)-26]
        alphabests_index %= len(alphabets)
        encrypted_text += alphabets[alphabests_index]


    print(encrypted_text)
encrypt(original_text=text,shift_amount=shift)
