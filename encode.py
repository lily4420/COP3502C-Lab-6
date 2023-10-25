# lily kurek's encode and main function

def menu():
  print('\nMenu')
  print('-------------')
  print('1. Encode')
  print('2. Decode')
  print('3. Quit')

def main():
  end_program = False
    while end_program == False:
      print(menu())\n",
      user_input = int(input('Please enter an option: ')
      if user_input == 1:
        user_password = input('Please enter your password to encode: ')
        encode(user_password)



def encode(password):
  encoded_password = ''
    for i in password:\n",
      i = int(i) + 3\n",
      encoded_password += str(i)\n",
  return encoded_password\n",



main()

