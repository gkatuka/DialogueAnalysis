# DialogueAnalysis

Data Pre-Processing 
In order to use this scripts ensure that the chat logs have been preprocessed and the dataset contains only the following columns:
[Corpus Utterance No, Session Utterance No, Time, Speaker, Utterance, Tag, SessionID] saved in a ,csv file e.g. taggeddataset.csv

In the command line: 
- Go to directory of your scripts
- Enter $ python ngram_gen.py taggeddataset.csv
- click enter 

//Generating bi-gram
Assuming no error: an output file will be generated in the same directory ngram_output.csv
The ngram_output will contain the [User, Ngram, Utterance 1, Utterance 2]

In the command line: 
- Go to directory of your scripts
- Enter $ python ngram_datatable.py ngram_output.csv
- click enter 

