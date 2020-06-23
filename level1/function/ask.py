def ask(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            print('invalid user response')
            break
        print(reminder)

if __name__ == '__main__':
    answer = ask('Do you really want to quit? ')
    print(answer)
    answer = ask('OK to overwrite the file? ')
    print(answer)
    answer = ask('quit? (y/n) ', 2, 'Come on, only yes or no!')
    print(answer)

