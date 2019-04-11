
'''

Applied Data Science 
Project 4 - Detection

'''

import glob
import pandas as pd
from sklearn.model_selection import train_test_split
from collections import defaultdict
from itertools import groupby

#import feature as feature


def labelTesseract():
        

    truth_counts = 0
    ground_tokens = []
    # create a list of all .txt files
    truth_files_list = glob.glob('../data/ground_truth/*.txt')
    # reading the ground truth file
    for file in truth_files_list:
        with open(file) as fd:
            for line in fd:
                each_line = line.strip().split()
                for word in each_line:
                    ground_tokens.append(word)
                    truth_counts += 1


    
    test_files_list = glob.glob('../data/tesseract/*.txt')

    # only taking the ones that have the same number of lines in the file

    truth_files = []
    test_files = []
    file_counts = 0 # store number of files (test and truth have same length)

    for truth, test in zip(truth_files_list, test_files_list):
        truth_length = len(open(truth).readlines())    
        test_length = len(open(test).readlines())
        if truth_length == test_length:
            file_counts += 1
            truth_files.append(truth)
            test_files.append(test)


    # only taking lines that have the same number of words
    truth_words = []
    test_words = []
    actual_counts = 0 # actual counts of numbers of words after filtering
    for truth, test in zip(truth_files, test_files):
            
        with open(truth) as fd_truth:
            with open(test) as fd_test:
                for truth_line, test_line in zip(fd_truth, fd_test):
                    tmp_truth = truth_line.strip().split()
                    tmp_test = test_line.strip().split()
                    if len(tmp_truth) == len(tmp_test):
                        for truth_word, test_word in zip(tmp_truth, tmp_test):
                            actual_counts += 1
                            truth_words.append(truth_word)
                            test_words.append(test_word)
    # uncomment below for testing
    
    print(actual_counts)
    print(len(truth_words))
    print(len(test_words))
    print(truth_words[:20])
    print(test_words[:20])
    
    
    '''
    # from the lists of words (truth, test) compare each of them
    # label 1 if test is the same as truth (correct)
    # label 0 if test is the different (wrong)

    label_dict = defaultdict(int)

    for truth, test in zip(truth_words, test_words):
        if truth == test:
            label_dict[test] = 1
        else:
            label_dict[test] = 0

    print(label_dict)
    '''

    # due to not being able to store duplicates, switching to list

    label = []
    for truth, test in zip(truth_words, test_words):
        if truth == test:
            label.append(1)
        else:
            label.append(0)
    
    # uncomment below for commenting
    
    print(label[:20])
    

    return (test_words, label)

def div_train(words, label, k = 0.2):

    data = pd.DataFrame(words)
    # split up data into k / 1-k percentage -- by defauly 80% train 20% test
    train_data, test_data, train_label, test_label = train_test_split(words, label, test_size = k)


    return (train_data, test_data, train_label, test_label)



def buildFeatures(train_data):
    # f1
    length = []
    
    # f2
    v_count = []
    c_count = []
    v_div_l = []
    c_div_l = []
    v_div_c = []
    
    # f3
    non_alnum = []
    non_alnum_div_l = []
    
    # f4
    digit = []
    digit_l = []

    # f5
    lower = []
    upper = []
    lower_div_l = []
    upper_div_l = []

    #f6
    three_consec_cons = []

    #f7
    alpha_num = []

    #f8
    six_consec_cons = []

    #f9
    infix = []

    for word in train_data:
        length.append(f_1(word))
        
        v_count.append(f_2(word)[0])
        c_count.append(f_2(word)[1])
        v_div_l.append(f_2(word)[2])
        c_div_l.append(f_2(word)[3])
        v_div_c.append(f_2(word)[4])
        
        non_alnum.append(f_3(word)[0])
        non_alnum_div_l.append(f_3(word)[1])

        digit.append(f_4(word)[0])
        digit_l.append(f_4(word)[1])

        lower.append(f_5(word)[0])
        upper.append(f_5(word)[1])
        lower_div_l.append(f_5(word)[2])
        upper_div_l.append(f_5(word)[3])

        three_consec_cons.append(f_6(word))

        alpha_num.append(f_7(word))

        six_consec_cons.append(f_8(word))

        infix.append(f_9(word))


    # create DataFrame

    df = pd.DataFrame({'length': length,
                       'num_vowels': v_count,
                       'num_conso': c_count,
                       'v_div_l': v_div_l,
                       'c_div_l': c_div_l,
                       'v_div_c': v_div_c,
                       'non_alnum': non_alnum,
                       'non_alnum_div_l': non_alnum_div_l,
                       'digit': digit,
                       'digit_l': digit_l,
                       'lower': lower,
                       'upper': upper,
                       'lower_div_l': lower_div_l,
                       'upper_div_l': upper_div_l,
                       'three_consec_cons': three_consec_cons,
                       'alpha_num': alpha_num,
                       'six_consec_cons': six_consec_cons,
                       'infix': infix})


    return df

def f_1(word):
    
    return len(word)

def f_2(word):
    l = len(word)
    vowels = 'aeiou'
    cons = 'bcdfghjklmnpqrstvwxyz'
    v_count = 0
    c_count = 0
    
    for c in word:
        if c in vowels:
            v_count += 1
        elif c in cons:
            c_count += 1


    if c_count == 0:
        return (v_count, c_count, v_count/l, c_count/l, 0)

    return (v_count, c_count, v_count/l, c_count/l, v_count/c_count)

def f_3(word):
    l = len(word)
    non_alnum = 0

    for c in word:
        if not c.isalnum():
            non_alnum += 1

    return (non_alnum, non_alnum/l)

def f_4(word):
    l = len(word)
    digit = 0

    for c in word:
        if c.isdigit():
            digit += 1
    return (digit, digit/l)

def f_5(word):
    l = len(word)
    upper = 0 
    lower = 0

    for c in word:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1 

    return (lower, upper, lower/l, upper/l)

def f_6(word):
    l = len(word)
    groups = groupby(word)
    result = [(label, sum(1 for _ in group)) for label, group in groups]

    max_count = float('-inf')
    for word_count in result:
        if word_count[1] > max_count:
            max_count = word_count[1]

    if max_count >= 3:
        return max_count/l
    else:
        return 0

def f_7(word):
    l = len(word)
    alnum = 0

    for c in word:
        if c.isalnum():
            alnum += 1
    
    non_alnum = l - alnum

    if non_alnum > alnum:
        return 1
    else:
        return 0

def f_8(word):
    cons = 'bcdfghjklmnpqrstvwxyz'
    consec_cons = 0
    max_count = 0

    for c in word:
        if c in cons:
            consec_cons += 1
        else:
            if max_count < consec_cons:
                max_count = consec_cons
            consec_cons = 0
    if max_count == 0:
        max_count = consec_cons

    if max_count >= 6:
        return 1
    else:
        return 0

def f_9(word):
    infix = word[1:-1]
    non_alnum = 0
    
    for c in infix:
        if not c.isalnum():
            non_alnum += 1
    if non_alnum >= 2:
        return 1
    else:
        return 0


if __name__ == '__main__':

    words, label = labelTesseract()
    train_data, test_data, train_label, test_label = div_train(words, label)
    print(train_data[:10])
    featureMatrix = buildFeatures(train_data)
    # uncomment for testing
    '''
    head = featureMatrix.head()
    print(head.to_string())
    '''

