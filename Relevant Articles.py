import glob
import os
'''
to work in make user enter number of keyword find all the
keyword then make the user enter article number
update irrelevant words
update all the code classes and add documentation
'''
def article_name_list():
    os.chdir('articles') #have problem here solve it!!!
    article_Files = glob.glob('*.txt')
    return article_Files
    
def read_File(article_Files):
    input_texts =[]
    for i in range(len(article_Files)):
        print(i+1,article_Files[i])
        file = open(article_Files[i])
        input_text = file.read()
        input_text = input_text.lower()
        input_texts.append(input_text)
    return input_texts


def word_lists(input_text):
    irrelevant_words = {".", "\n", 'the',"what", "and",
    "is", "was", "he", "at", "to", "for", "can",'of', 'in'
    , 'also', 'after',"a",'are','we','as', 'our','on', 'that','it','by',
    'have', 'this', 'but','been', 'be', 'has','their','with', 'or','will'
    ,'from','they', 'you','not','most','her', 'she','his','--','mr','told',
    '-','mr.','were','had','how','while','said','had','many','its','i','my'
    ,'an','who','about','would', 'so','which','says','when', 'just','us','want'
    ,'more','get','use','some','than','then','made',
    'because','such',
    'him','go',
    'over'
    'me'}
    
    word_list = input_text.split(" ")
    for iw in irrelevant_words:
        for j in range(len(word_list)):
            if word_list[j] == iw:
                word_list[j] = ""
        # input_text = input_text.replace(iw, "")
    return word_list


def histogram(word_list):
   word_histogram = {
   }
   for word in word_list:
       if word not in word_histogram.keys():
           word_histogram[word] = 1
       else:
           word_histogram[word] = word_histogram[word] + 1
   word_histogram.pop("")
   return word_histogram


def article_keyword(my_dict):
    x=list(my_dict.values())
    x.sort(reverse=True)
    x=x[:4]
    x = [*set(x)]
    keywords = []
    for i in x:
       
        for j in my_dict.keys():
            if(my_dict[j]==i):
                keywords.append(j)
    return keywords


def relavent(keyword1,keyword2,file):
    c=0
    for i in range(len(keyword1)):
        for j in range(len(keyword2)):
            if keyword1[i] == keyword2[j]:
                c = c+1
    return [c,file]


def the_Most_Intersection(keyword1,keyword2,files):##problem!!   
    r=[]
    for i in range(len(keyword2)):
        re = relavent(keyword1,keyword2[i],files[i])
        r.append(re)
    
    q=[]
    maxi = max(r)
    if maxi[0] != 0:
       for i in range(len(r)):
           if maxi[0] == r[i][0]:
               q.append(r[i][1]) 
       return q
    else:
       return("no relative article!!!!")
        
   
    
      


#convert to classes
list_of_article = article_name_list()
article_texts = read_File(list_of_article)
main_article_number = int(input("enter the number of article you want to find it relevants"))
main_article = article_texts[main_article_number-1]
main_article_name = list_of_article[main_article_number-1]
article_texts.remove(main_article)
list_of_article.remove(main_article_name)




main_article_dictionary = histogram(word_lists(main_article))
main_keyword = article_keyword(main_article_dictionary)
# find the histograme for each file text
keywords = []
for i in range(len(article_texts)):
    article_dictionary = histogram(word_lists(article_texts[i]))
    keyword = article_keyword(article_dictionary)
    keywords.append(keyword)
    

 
    
print("articles with the most intersection",the_Most_Intersection(main_keyword,keywords,list_of_article)   )    

 