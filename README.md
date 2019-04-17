# Project: OCR (Optical Character Recognition) 

![image](figs/intro.png)

### [Full Project Description](doc/project4_desc.md)


+ Team **Spring 2019**
+ Team members
	+ HyunBin Yoo hy2506@columbia.edu
	+ Guanren Wang gw2380@columbia.edu
	+ Andy Huang yh3090@columbia.edu
	+ Feng Su fs2658@columbia.edu
	+ Ying Jin yj2453@columbia.edu

+ Project summary: 

In this project, we created an OCR post-processing procedure to enhance Tesseract OCR output. For dectection we used the D-3 method which includes feature engineering and training the Support Vector Machine (SVM) for the classification. First, we labelled tesseract using the ground truth, but we ignored the files with different number of lines and lines with different number of words. For the improvement, we could have implemented a way to include all the files and all the lines. Each feature was built using separate functions and Buildfeature fuction is used to aggregate all the features and to create a feature matrix. Then the result was fed into SVM for training. Training took about 30 mins. As a result, the weighted average precision is 0.83 and the weighed average recall is 0.84. Overall, the weighted average f1-score is 0.83.

For correction part, we used C-3 method which can help us to detect those words containning exact one typos on the test data from detection part. First, we used edit distance to find each typo's potential correction candidates. Then we used Bayesian combination rule to choose the most possible correction. And the algorithm we used to calcaute the pr(t|c) is stated as following:

	+ del[cp_ 1, cp]/chars[cp-1, cp] if deletion
	+ add[cp_ l, tp]/chars[cp-l]  if insertion
	+ sub[tp, Cp]/chars[cp] if substitution 
	+ rev[cp, cp + l]/chars[cp, cp + 1] if reversal 
	
We should be careful when we deal with the cases then the index of position of correction equal to 0 since in these cases, we don't have any information about cp-1 and according to the advice of professor,we calculate the number of words in training set instead which is also quite rational. The method we use to calcuate pr(c) is ELE and the posterior probility pr(c)*pr(t|c). 

We evaluated our algorithm using precision and recall, in both word level and character level. And the result shows that we improved the word precision from 0.67 to 0.77; word recall from 0.66 to 0.75; character precision from 0.94 to 0.96; character recall from 0.91 to 0.94, which is a significant enhancement to the tesseract.

**Contribution statement**: 

Project: OCR Post-Processing

Team members: HyunBin Yoo, Guanren Wang, Andy Huang, Feng Su, Ying Jin.

HyunBin Yoo and Guanren Wang discussed on how to label the data for SVM training and which features would be appropriate as the features to SVM and developed the detection SVM model. HyunBin Yoo implemented the detection part algorithm in python. Andy Huang, Feng Su and Ying Jin discussed, explored the correction model and designed, carried out the evaluation part. All team members contributed to the GitHub repository and prepared the presentation. As a presenter, HyunBin Yoo created the powerpoint slide. All team members approve our work presented in our GitHub repository including this contribution statement.
	
Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
