secret_no=9
guess_count=0
guess_limit=3
while guess_count<=guess_limit:
    guess = int(input('guess: '))
    guess_count+=1
    if guess==secret_no:
        print('winer')
        break
else:
    print('failed')

