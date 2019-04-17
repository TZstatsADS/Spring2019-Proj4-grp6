# Project: OCR (Optical Character Recognition) 

![image](figs/intro.png)

### [Full Project Description](doc/project4_desc.md)


+ Team **Spring 2019**
+ Team members
	+ HyunBin Yoo hy2506@columbia.edu
	+ Guanren Wang gw2380@columbia.edu
	+ Yunhao Huang yh3090@columbia.edu
	+ Feng Su fs2658@columbia.edu
	+ Ying Jin yj2453@columbia.edu

+ Project summary: In this project, we created an OCR post-processing procedure to enhance Tesseract OCR output. For dectection we used the D-3 method which includes feature engineering and training the Support Vector Machine (SVM) for the classification. First, we labelled tesseract using the ground truth, but we ignored the files with different number of lines and lines with different number of words. For the improvement, we could have implemented a way to include all the files and all the lines. Each feature was built using separate functions and Buildfeature fuction is used to aggregate all the features and to create a feature matrix. Then the result was fed into SVM for training. Training took about 30 mins. 
	
**Contribution statement**: ([default](doc/a_note_on_contributions.md)) All team members contributed equally in all stages of this project. Hyunbin Yoo and Guanren Wang worked on detection part together, while Yunhao Huang, Feng Su and Ying Jin worked on correction part. All team members approve our work presented in this GitHub repository including this contributions statement. 

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
