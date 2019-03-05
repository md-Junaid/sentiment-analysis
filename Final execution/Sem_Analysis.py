

#sentimental analysis
from textblob import TextBlob
class Sem_Analysis:
    count_positive = 0
    count_negative = 0
    count_neutral = 0
    Average_polarity = 0
    Average_subjectivity = 0
    percent_positive=''
    percent_negative=''
    percent_neutral=''
    def sent_tweet(self,fname):   
        count_positive = 0
        count_negative = 0
        count_neutral = 0
        Average_polarity = 0
        Average_subjectivity = 0
        total_tweets=0
        lst1=[]
        lst2=[]
        f = open(fname,'r')
        f1= f.readlines()
        for line in f1:
            sent1 = TextBlob(line)
            tb1 = sent1.sentiment.polarity
            lst1.append(tb1)
            tb2 = sent1.sentiment.subjectivity
            lst2.append(tb2)
        for item in lst1:
            if item>0:
                count_positive += 1
            elif item<0:
                count_negative +=1
            else:
                count_neutral +=1
        self.count_positive = count_positive
        self.count_negative = count_negative
        self.count_neutral = count_neutral
        total_tweets = count_positive + count_negative + count_neutral
        self.percent_positive = str(round(count_positive/total_tweets*100 ,4)) + "%"
        self.percent_negative = str(round(count_negative/total_tweets*100 ,4)) +"%"
        self.percent_neutral = str(round(count_neutral/total_tweets*100 ,4)) +"%"

        Average_polarity = sum(lst1)/len(lst1)
        self.Average_polarity = round(Average_polarity,4)
        Average_subjectivity = sum(lst2)/len(lst2)
        self.Average_subjectivity = round(Average_subjectivity,4)
        #print ("Positive : ",count_positive,"\nNegative : ", count_negative,"\nNeutral : ",count_neutral)
        #print("Average polarity : ", Average_polarity,"Average Subjectivity : ",Average_subjectivity)

