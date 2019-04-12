
'''

Applied Data Science 
Project 4 - Detection

'''

import glob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import collections
from collections import defaultdict
from itertools import groupby
import nltk

#import feature as feature


def labelTesseract():
        

    
    truth_files_list = glob.glob('../data/ground_truth/*.txt') 
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
    truth_test_pair = [] # for correction
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
                            truth_test_pair.append((truth_word, test_word))
    # uncomment below for testing
    ''' 
    print(actual_counts)
    print(len(truth_words))
    print(len(test_words))
    print(truth_words[:20])
    print(test_words[:20])
    '''
    
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
    '''
    print(label[:20])
    '''

    return (truth_test_pair, test_words, label)

def div_train(pair, label, k = 0.2):

    # data = pd.DataFrame(words)
    # split up data into k / 1-k percentage -- by defauly 80% train 20% test
    train_data, test_data, train_label, test_label = train_test_split(pair, label, test_size = k)

    X_train = []
    X_test = []
    X_train_truth = []
    X_test_truth = []
    for data in train_data:
        X_train.append(data[1])
        X_train_truth.append(data[0])
    for data in test_data:
        X_test.append(data[1])
        X_test_truth.append(data[0])



    return (X_train, X_test, train_label, test_label, X_train_truth, X_test_truth)



def buildFeatures(train_data, bigram_dict):
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

    #f10
    bigram = []

    #f11
    most_freq = []

    #f12
    non_div_alpha = []

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

        # can change the scaling constant (third parameter)
        bigram.append(f_10(word, bigram_dict, 10000))

        most_freq.append(f_11(word))

        non_div_alpha.append(f_12(word))




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
                       'infix': infix,
                       'bigram': bigram,
                       'most_freq': most_freq,
                       'non_div_alpha': non_div_alpha})


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

def f_10(word, bigram_dict, c = 10000):

    word = word.lower()
    count = 0.0
    naturalness = 0.0
    for i in range(len(word)-1):
        count += 1.0
        naturalness += bigram_dict[(word[i], word[i+1])] / c

    return naturalness

# return frequency of most frequent symbol
def f_11(word):
    l = len(word)
    most_freq = collections.Counter(word).most_common(1)[0][1]

    if most_freq >= 3:
        return most_freq/l
    else:
        return 0

def f_12(word):
    l = len(word)
    alpha = 0

    for c in word:
        if c.isalpha():
            alpha += 1

    non_alpha = l - alpha
    if alpha == 0:
        return 0
    
    return non_alpha / alpha

def compute_bigram():
    
    bigram_dict = defaultdict(int)
    truth_files_list = glob.glob('../data/ground_truth/*.txt')
    for file in truth_files_list:
        with open(file) as fd:
            for line in fd:
                each_line = line.strip().split()
                for word in each_line:
                    word = word.lower()
                    for i in range(len(word)-1):
                        bigram_dict[(word[i], word[i+1])] += 1

    return bigram_dict

if __name__ == '__main__':

    pair, words, label = labelTesseract()
    train_data, test_data, train_label, test_label, ground_truth_train, ground_truth_test = div_train(pair, label)

    # uncomment to test for truth, tesseract pair
    '''
    print(train_data[:10])
    print(ground_truth_train[:10])
    print(train_label[:10])
    
    print(test_data[:10])
    print(ground_truth_test[:10])
    print(test_label[:10])
    '''

    
    bigram_dict = compute_bigram()
    featureMatrix_train = buildFeatures(train_data, bigram_dict)
    featureMatrix_test = buildFeatures(test_data, bigram_dict)
    
    # uncomment for testing
    '''
    head = featureMatrix_train.head()
    print(head.to_string())
    '''

    # build classifier
    svm_class = SVC(kernel='rbf', verbose=True, gamma='scale')
    svm_class.fit(featureMatrix_train, train_label)

    # prediction
    prediction = svm_class.predict(featureMatrix_test)

    output = pd.DataFrame({'data': test_data,
                           'label': prediction})
    
    print(output[:20])

    ##### evaluation
    #confustion Matrix
    from sklearn.metrics import classification_report, confusion_matrix
    
    print(confusion_matrix(test_label, prediction))
    print(classification_report(test_label, prediction))

   
