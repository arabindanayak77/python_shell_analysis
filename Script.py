
# coding: utf-8

# In[ ]:



# In[1]:

import pandas
import sys
import matplotlib.pyplot as plt


filename = sys.argv[1]

human_chr21 = pandas.read_csv(filename, sep="\t")
human_chr21["gc_content"] = human_chr21['gc_bases']/(human_chr21['win_end']-human_chr21['win_start'])
human_chr21["gene_content"] = human_chr21['exon_bases']/(human_chr21['win_end']-human_chr21['win_start'])

# %matplotlib inline
plt.plot(human_chr21["gene_content"],human_chr21["gc_content"],"o")
plt.xlabel("Exon Bases")
plt.ylabel("GC Content")

plt.savefig(filename + '.plot.png')


# In[]

