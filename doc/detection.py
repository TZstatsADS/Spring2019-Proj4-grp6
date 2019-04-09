
'''

Applied Data Science 
Project 4 - Detection

'''

import glob
from collections import defaultdict


def parseGroundTruth():
        
    truth_dict = defaultdict(int)

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

    for truth, test in zip(truth_files, test_words):
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



        
    

if __name__ == '__main__':

    parseGroundTruth()

