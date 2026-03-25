from art import  logo

alphabets=['a','b', 'c', 'd' ,'e', 'f', 'g' ,'h', 'i','j', 'k', 'l' ,'m' ,'n', 'o', 'p' ,'q' ,'r',
         's' ,'t' ,'u' ,'v','w', 'x', 'y', 'z']
print(logo)


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for i in original_text:
        if i not in alphabets:
            output_text += i
        else:
            shifted_index = alphabets.index(i) + shift_amount
            shifted_index %= len(alphabets)
            output_text += alphabets[shifted_index]

    print(f"your {encode_or_decode}d text is: {output_text}")



run = True
while run:
    direction = input("Type encrypt to Encrypt and decrypt to Decrypt:\n" ).lower()
    text = input("Enter the text:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    caesar(text, shift, direction)
    user_choice = input("Type yes to continue otherwise no to stop\n").lower()
    if user_choice == "no":
        run = False
        print("Good Bye!")
