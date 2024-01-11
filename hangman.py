import random

def hangman():
    wordlist = ["cat", "dog", "bird", "insect", "hippopotamus", "zebra"]

    wordcounts = 0
    for i, words in enumerate(wordlist):
        words = wordlist[i]
        wordcounts += 1

    wordnumber = random.randint(0, wordcounts - 1)

    word = wordlist[wordnumber + 1]

    print("wordcounts is", wordcounts)
    
    wrong = 0
    stages = ["",
              "┏━━━━━━━━━━━┳　　　　",
              "┃　　　　　　　┃　　　　",
              "┃　　　　　　　┃　　　　",
              "┃　　　　　　　⚫︎　　　　",
              "┃　　　　　　┏ ╂ ┓　　　",
              "┃　　　　　　　┃┃　　　",
              "┃　　　　　　　 　　　　"
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("HANG-MAN")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してください。"
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print("その文字はあります！")
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You win!!!")
            print(" ".join[board])
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose....ANSWER is {}".format(word))
