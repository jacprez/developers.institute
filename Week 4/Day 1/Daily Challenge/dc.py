user_inp = input("Enter a 10 letter word: ")
if len(user_inp) < 10:
    print("Too short, goodbye.")
elif len(user_inp) > 10:
    print("Too long, goodbye.")
elif len(user_inp) == 10:
    build_up = ""
    for i in range(len(user_inp)):
        if i == 0:
            print(f"the first letter is {user_inp[0]} and the last letter is {user_inp[-1]}")
        build_up += user_inp[i]
        print(build_up)


