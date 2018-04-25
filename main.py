'''
Anish Shenoy
SoftDev2 pd07
K15 -- Do You Even List?
2018-04-25
'''

UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = ".?!&#,;:-_*"

def min_thresh(p):

    print "Password: " + p

    upper_lower_sum = sum([1 if x in UPPER_LETTERS else 0 for x in p])
    len_no_nums = sum([0 if x in NUMBERS else 1 for x in p])
    number_sum = sum([1 if x in NUMBERS else 0 for x in p])

    upper_lower_bool = 0 < upper_lower_sum < len_no_nums
    number_bool = number_sum > 0
    val = upper_lower_bool and number_bool

    '''
    if upper_lower_bool:
        print "Mixed Case checked"
    if number_bool:
        print "Has number" '''

    print val
    print

    return val

min_thresh("wknfjeew")
min_thresh("wkNNfjeew")
min_thresh("wknfjeew1")
min_thresh("EREGREG23")
min_thresh("EF3WFeEWwefe2fFWE3")

def strength_rating(p):
    bool_to_score = {True: 10, False: 0}

    print "Password: " + p

    upper_lower_sum = float(sum([1 if x in UPPER_LETTERS else 0 for x in p]))
    len_no_nums = float(sum([0 if x in NUMBERS else 1 for x in p]))
    number_sum = float(sum([1 if x in NUMBERS else 0 for x in p]))
    special_sum = float(sum([1 if x in SPECIAL else 0 for x in p]))

    upper_lower_score = (0.5 - abs(0.5 - (upper_lower_sum / len_no_nums))) * 20
    number_score = bool_to_score[(number_sum > 0)]
    special_score = bool_to_score[(special_sum > 0)]

    print "Case Score: "
    print upper_lower_score
    print "Number Score: "
    print number_score
    print "Special Score: "
    print special_score
    print "Final Score: "

    score_list = [upper_lower_score, number_score, special_score]
    score = sum([(x/3) for x in score_list])

    print score
    print
    return score

strength_rating("aaaaaaaa")
strength_rating("aaaaaaaAAAAA")
strength_rating("aaaaaa123AAAAA")
strength_rating("aaaaaaaAAAAA**")
strength_rating("aaaaaAAAAA123443343242356__?!&")
strength_rating("dnWW12??")
