
'''

Applied Data Science 
Project 4 - Detection

'''

import glob
from collections import defaultdict


def parseGroundTruth():
        
    truth_dict = defaultdict(int)
    truth_count = 0
    ground_tokens = []
    # create a list of all .txt files
    truth_files = glob.glob('../data/ground_truth/*.txt')
    # reading the ground truth file
    for file in truth_files:
        with open(file) as fd:
            for line in fd:
                each_line = line.strip().split()
                for word in each_line:
                    ground_tokens.append(word)
    print(len(ground_tokens))
    print(ground_tokens[:20])

        
    

if __name__ == '__main__':

    parseGroundTruth()

