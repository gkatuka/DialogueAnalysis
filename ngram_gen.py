#In command line/ terminal 
# python3 ngram_gen.py "sample_corpus1.csv"

import sys, csv
import pandas as pd 

#sys.argv will contain["python", "ngram_gen.py", "sample_corpus1.csv"]
if len(sys.argv) >1:
    infile =  sys.argv[1]
    with open(infile, encoding='ISO-8859-1') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        writer = csv.writer(open('output_corpus1.csv', 'w'))
        writer.writerow(["User", "NGram", "Utterance_1",
                     "Utterance_2"])

        next(readCSV)
    
        tupleList = []
        
         # Populates tuple list of 0: Sesssion Utterance ID, 1:User Name, 2:Tag, 3:Utterance
        for row in readCSV:
            tupleList.append((row[0], row[2], row[5], row[4]))

        entered_partner_loop = False

        unigram_counter = 0

        #print(len(tupleList))

    
        set_student = ""
        second_student_counter = 0
        for i in range(len(tupleList)):
            if(tupleList[i][0] == "1"):
                set_student = tupleList[i][1]
                entered_partner_loop = False
                second_student_counter = i

            if(set_student != tupleList[i][1] and entered_partner_loop == False):
                entered_partner_loop = True
                set_student_2 = tupleList[i][1]

                for x in range(len(tupleList))[second_student_counter:]:
                    if(tupleList[x][0] == "1" and tupleList[x][1] != set_student):
                        break

                    else:
                        if(set_student_2 == tupleList[x][1]):
                            writer.writerow(
                                [set_student_2, tupleList[x][2] + "_stu", tupleList[x][3]])

                            unigram_counter += 1

                        if(set_student_2 != tupleList[x][1]):
                            writer.writerow(
                                [set_student_2, tupleList[x][2] + "_par", tupleList[x][3]])

                            unigram_counter += 1

            else:
                if(set_student == tupleList[i][1]):
                    writer.writerow(
                        [set_student, tupleList[i][2] + "_stu", tupleList[i][3]])

                if(set_student != tupleList[i][1]):
                    writer.writerow(
                        [set_student, tupleList[i][2] + "_par", tupleList[i][3]])

        entered_partner_loop = False

        bigram_counter = 0

        # TODO: Change x and i to better names
        for i in range(len(tupleList) - 1):
            if(tupleList[i][0] == "1"):
                set_student = tupleList[i][1]
                entered_partner_loop = False
                second_student_counter = i

            if(set_student != tupleList[i][1] and entered_partner_loop == False):
                entered_partner_loop = True
                set_student_2 = tupleList[i][1]

                for x in range(len(tupleList) - 1)[second_student_counter:]:
                    if(tupleList[x + 1][0] == "1"):
                        break

                    else:
                        if(set_student_2 == tupleList[x][1]):
                            if(set_student_2 == tupleList[x + 1][1]):
                                writer.writerow([set_student_2, tupleList[x][2] + "_stu" + ", " +
                                                tupleList[x + 1][2] + "_stu", tupleList[x][3], tupleList[x + 1][3]])

                                bigram_counter += 1

                            if(set_student_2 != tupleList[x + 1][1]):
                                writer.writerow([set_student_2, tupleList[x][2] + "_stu" + ", " +
                                                tupleList[x + 1][2] + "_par", tupleList[x][3], tupleList[x + 1][3]])

                                bigram_counter += 1

                        if(set_student_2 != tupleList[x][1]):
                            if(set_student_2 == tupleList[x + 1][1]):
                                writer.writerow([set_student_2, tupleList[x][2] + "_par" + ", " +
                                                tupleList[x + 1][2] + "_stu", tupleList[x][3], tupleList[x + 1][3]])

                                bigram_counter += 1

                            if(set_student_2 != tupleList[x + 1][1]):
                                writer.writerow([set_student_2, tupleList[x][2] + "_par" + ", " +
                                                tupleList[x + 1][2] + "_par", tupleList[x][3], tupleList[x + 1][3]])

                                bigram_counter += 1

            # Checks if one ahead is start of new session, ignores
            if(tupleList[i + 1][0] == "1"):
                continue

            else:
                if(set_student == tupleList[i][1]):
                    if(set_student == tupleList[i + 1][1]):
                        writer.writerow([set_student, tupleList[i][2] + "_stu" + ", " +
                                        tupleList[i + 1][2] + "_stu", tupleList[i][3], tupleList[i + 1][3]])

                    if(set_student != tupleList[i + 1][1]):
                        writer.writerow([set_student, tupleList[i][2] + "_stu" + ", " +
                                        tupleList[i + 1][2] + "_par", tupleList[i][3], tupleList[i + 1][3]])

                if(set_student != tupleList[i][1]):
                    if(set_student == tupleList[i + 1][1]):
                        writer.writerow([set_student, tupleList[i][2] + "_par" + ", " +
                                        tupleList[i + 1][2] + "_stu", tupleList[i][3], tupleList[i + 1][3]])

                    if(set_student != tupleList[i + 1][1]):
                        writer.writerow([set_student, tupleList[i][2] + "_par" + ", " +
                                        tupleList[i + 1][2] + "_par", tupleList[i][3], tupleList[i + 1][3]])

        entered_partner_loop = False

        #writer.writerow(["Unigrams: " + str(unigram_counter), "Bigrams: " + str(bigram_counter)])
        print("Total Number of Unigrams: " + str(unigram_counter))
        print("Total Number of Bigrams: " + str(bigram_counter))
        print("Total Number of Ngrams: " + str(unigram_counter + bigram_counter))


