def calculate_scores():
    print("O'yinchi 1 harakatlarini kiriting (masalan: share, steal):")
    P1 = input().strip().split(", ")
    print("O'yinchi 2 harakatlarini kiriting (masalan: share, steal):")
    P2 = input().strip().split(", ")

    firs_player = 3  
    second_player = 3

    for 1, 2 in zip(P1, P2):
        if 1 == "share" and 2 == "share":
            firs_player += 2
            second_player += 2
        elif 1 == "share" and 2 == "steal":
            firs_player += 0
            second_player += 3
        elif 1 == "steal" and 2 == "share":
            firs_player += 3
            second_player += 0
        elif 1 == "steal" and 2 == "steal":
            firs_player += 1
            second_player += 1

    print("Natija: [", firs_player, ",", second_player, "]")

calculate_scores()
