import matplotlib.pyplot as plt
import numpy as np


def create_labels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x()+ item.get_width()/2., height * 1.05,
                  height, ha='center', va='bottom')

COL_COUNT = 3
BAR_WIDTH = .1
ALPHA = .4

LABELS = ("Math", "Reading", "Science")

korea_scores  = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores  = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(COL_COUNT)

k1 = plt.bar(index, korea_scores,  BAR_WIDTH, alpha=ALPHA, label="Korea")
c1 = plt.bar(index + BAR_WIDTH, canada_scores, BAR_WIDTH, alpha=ALPHA, label="Canada")
x1 = plt.bar(index + 2*BAR_WIDTH, china_scores, BAR_WIDTH, alpha=ALPHA, label="China")
f1 = plt.bar(index + 3*BAR_WIDTH, france_scores, BAR_WIDTH, alpha=ALPHA, label="France")
SCORES = [k1, c1, x1, f1]


for item in SCORES:
    create_labels(item)

plt.xticks(index + .3 / 2, LABELS)

plt.xlabel("Subject")
plt.ylabel("Mean Score in PISA 2012")

plt.title("Test scores by Country")

plt.legend(frameon=False, bbox_to_anchor=(1,1), loc=2 )
plt.grid(True)



plt.show()
