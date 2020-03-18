user_input = input('please input username: ')
print("Hello {}, let's play Hangman".format(user_input))

word = 'rahasia'
guess = ''
turns = len(word)*2

while turns > 0:
    failed = 0
    for alph in word:
        if alph in guess:
            print(alph, end=" ")
        else:
            print('_',end=" ")
            failed += 1
    if failed == 0:
        print('\n\n{} You win!'.format(user_input))
        break
    print()
    huruf = input('masukkan huruf: ')
    guess += huruf
    if guess not in word:
        turns -= 1
        print('wrong, you have {} turns.'.format(turns))
    if turns == 0:
        print("You lose!")