
number_of_decks=1
deck = {
    1: 4*number_of_decks,
    2: 4*number_of_decks,
    3: 4*number_of_decks,
    4: 4*number_of_decks,
    5: 4*number_of_decks,
    6: 4*number_of_decks,
    7: 4*number_of_decks,
    8: 4*number_of_decks,
    9: 4*number_of_decks,
    10: 16*number_of_decks, }


def updated_deck(array_of_cards):
    global deck
    a = dict(deck)
    updated = {}
    for i in array_of_cards:
        a[i] -= 1

    for i in a:
        if a[i] > 0:
            updated[i] = a[i]

    return updated

def get_total(array_of_cards):
    total = 0
    ace_num = 0
    for i in array_of_cards:
        if i == 1:
            ace_num += 1

        else:
            total += i

    if ace_num > 0:
        sums = []
        for i in range(0, ace_num + 1):
            newtot = total + i + (11 * (ace_num - i))
            if newtot <= 21:
                sums.append(newtot)

        if len(sums) > 0:
            sums = sorted(sums)
            return sums[-1]
        else:
            return total + ace_num




    else:
        return total


def bust_cases(array_of_cards):
    """     Returns : [bustcasesarray,nobustcasesarray,buscaseinteger,nobustcseinteger] """

    global deck
    total = get_total(array_of_cards)

    bust_case = 0
    no_bust_case = 0

    busted = []
    not_busted = []
    for i in deck:

        new_cards = []
        for j in array_of_cards:
            new_cards.append(j)

        new_cards.append(i)

        new_total = get_total(new_cards)

        if new_total > 21:
            bust_case += deck[i]
            busted.append(new_cards)


        else:
            # less than 21
            no_bust_case += deck[i]
            not_busted.append(new_cards)

    return [busted, not_busted, bust_case, no_bust_case]


def draw_1_card(array_of_cards):
    """Returns an array of arrays. The sub-arrays are all the possible cases that can happen when a card is drawn."""
    global deck
    updated = updated_deck(array_of_cards)
    all = []
    for i in updated:
        a = []
        for x in array_of_cards:
            a.append(x)
        a.append(i)
        all.append(a)

    return all


def card_analysis(your_array_of_cards, oppponent_array_of_cards):
    """Given two decks of cards, analyses the probability of the player winning, losing, and there being a draw.
    Returns: [scenarios_won,scenarios_drawn,scenarios_lost]. All of the numbers in the array are integers."""
    win = 0
    lose = 0
    draw = 0
    mytotal = get_total(your_array_of_cards)

    if len(your_array_of_cards) >= 5 and mytotal <= 21:
        return [1, 0, 0]

    elif mytotal==21:
        return [1,0,0]

    cards = draw_1_card(oppponent_array_of_cards)

    for c in cards:

        total = get_total(c)
        if total >= 17 or len(c) >= 4:
            if mytotal == total:
                draw += 1
                # print(str(c)+"  D")


            elif total == 21:
                lose += 1

                # print(str(c)+"  L")

            elif total > 21:
                win += 1

                # print(str(c)+"  W")

            elif mytotal > total:
                win += 1

                # print(str(c)+"  W")


            else:
                lose += 1

                # print(str(c)+"  L")

        else:
            try_again = card_analysis(your_array_of_cards, c)
            win += try_again[0]
            draw += try_again[1]
            lose += try_again[2]

    a = [win, draw, lose]
    return a


def winning_probability(your_array, opponent_array):
    """Converts the number of cases from the function 'card_analysis' into probabilities.
    Returns: [win_probability, draw_probability, lose_probability]. (All probabilities are in the perspective of the
    player who has the hand labeled 'your_array')."""
    a = card_analysis(your_array, opponent_array)

    return [a[0] / (a[0] + a[2]),
            a[1] / (a[0] + a[1] + a[2]),
            a[2] / (a[0] + a[2])]


def bust_probability(your_array):
    """Returns the probability of the given hand to bust (go over 21 and automatically lose the game). """
    a = bust_cases(your_array)

    return a[-2] / (a[-1] + a[-2])


def hit_win_prob(array_of_initial_cards, opponent_cards):
    """Analyzes the overall probability of the player winning, if they draw one card."""
    cards = draw_1_card(array_of_initial_cards)
    won = 0
    allcases = 0
    b = []
    blackjacks = []

    for c in cards:

        total = get_total(c)
        results = card_analysis(c, opponent_cards)
        if total == 21:
            won += results[0]
            blackjacks.append(c)

        elif total < 21:
            won += results[0]
            b.append(c)

        allcases = allcases + results[0]+ results[2]

    return [won / allcases, b, blackjacks]


def all_cases(you, memer):
    win_as_is = winning_probability(you, memer)[0]
    bust_prob = bust_probability(you)
    # no_bust_prob=1-bust_prob

    draw1_prob = hit_win_prob(you,memer)
    paralel_timelines = draw1_prob[1]
    blackjacks = draw1_prob[2]
    draw1_prob = draw1_prob[0]

    draw2_prob_sums = 0
    paralel2 = []
    for c in paralel_timelines:
        asd = hit_win_prob(c,memer)
        variations = asd[1]
        draw2_prob_sums += asd[0]

        for x in variations:
            paralel2.append(x)

    try:
        draw2_prob_sums = draw2_prob_sums / len(paralel_timelines)

    except ZeroDivisionError:
        draw2_prob_sums = draw2_prob_sums / len(blackjacks)

    draw3_prob_sums = 0
    paralel3 = []
    for c in paralel2:
        asd = hit_win_prob(c,memer)
        variations = asd[1]
        draw3_prob_sums += asd[0]

        for x in variations:
            paralel3.append(x)

    try:
        draw3prob = draw3_prob_sums / len(paralel3)
    except ZeroDivisionError:
        draw3prob = 0

    return [win_as_is, draw1_prob, draw2_prob_sums, draw3prob]


def get_move(your_cards, opponent_cards):
    """Returns the optimal move for the player. If the player should hit, returns 'h'. If the player should stand,
    returns 's'. This function basically compares the probability of your current hand winning versus the probability
    of you to wing if you draw 1 card. """

    win_as_is = winning_probability(your_cards, opponent_cards)[0]
    draw1_prob = hit_win_prob(array_of_initial_cards=your_cards, opponent_cards=opponent_cards)[0]

    if draw1_prob > win_as_is:
        return "h"
    else:
        return "s"


def calculate_house_edge():
    """Calculates the house edge for the given rules. Goes over all possible scenarios. Due to the recursive nature
    of the algorithms and the quantitiy of possible scenarios, the process may take a while. """
    total=0
    cases=0
    for i in deck:
        for j in deck:

            cards=[i,j]
            print(cards)
            for m in deck:
                winpo=all_cases(cards,[m])
                winpo=sorted(winpo) #ascending order
                #print(asdf,cards,m,winpo[-1])

                total+=winpo[-1]
                cases+=1
    return(total/cases)
