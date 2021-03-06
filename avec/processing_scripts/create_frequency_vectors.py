import csv
import pandas as pd
import numpy as np
import os

from clean_text import *
from process_corpus_vectors import *

from sklearn.feature_extraction.text import CountVectorizer


#change directory
train_text_dir_raw = './trainPart/raw/'
train_text_dir_with_i = './trainPart/cleaned_with_i'

dev_text_dir_raw = './devPart/raw/'
dev_text_dir_with_i = './devPart/cleaned_with_i'

test_text_dir_raw = './testPart/raw/'
test_text_dir_with_i = './testPart/cleaned_with_i'

#only process TXT files, set files in /raw/ folders to process differently
file_ends_with = '.txt'
dir_ends_with = 'raw'

#save output with different filenames
to_save_train = 'X_train_raw.npy'
to_save_train_clean = 'X_train_cleaned_with_i.npy'

to_save_dev = 'X_dev_raw.npy'
to_save_dev_clean = 'X_dev_cleaned_with_i.npy'

to_save_test = 'X_test_raw.npy'
to_save_test_clean = 'X_test_cleaned_with_i.npy'

#list to append each transcript to
docs = []

#change these variables here:
chdir = dev_text_dir_raw
to_save = to_save_dev

#create frequency vectors here
frequency_vectors(docs, chdir, file_ends_with, dir_ends_with, to_save)
