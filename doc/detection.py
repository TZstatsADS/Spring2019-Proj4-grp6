
'''

Applied Data Science 
Project 4 - Detection

'''

import glob
import pandas as pd
from collections import defaultdict


def parseGroundTruth():
        

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



def buildFeatures():

def f1_length():

def f2_num_vowels():

def f3_num_cons():

def f4_v_div_l():

def f5_c_div_l():
        
def f6_v_div_c():

def f7_num_spec_sym():

def f8_d_div_l():

def f9_num_lower():

def f10_num_upp():

def f11_lower_div_l():

def f12_upp_div_l():

 __name__ == '__main__':

    parseGroundTruth()

