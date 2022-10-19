import glob
import os


def article_name_list(folder_name ='articles'):
    """
    Return a list  of all files name
    in 'articles' folder
    """
    os.chdir(folder_name) 
    articles_name = glob.glob('*.txt')
    return articles_name
 
   
def read_file(files_name):
    """
    Open and read  files
    Return the texts converted 
    to lowercase
    """
    file = open(files_name)
    input_text = file.read()
    input_text = input_text.lower()
    return input_text


def word_lists(input_text):
    """
    Get rid of irrelevant words 
    Return list of the words in file text
    """
    irrelevant_words = {".", "\n", 'the',"what", "and",
    "is", "was", "he", "at", "to", "for", "can",'of', 'in'
    , 'also', 'after',"a",'are','we','as', 'our','on', 'that','it','by',
    'have', 'this', 'but','been', 'be', 'has','their','with', 'or','will'
    ,'from','they', 'you','not','most','her', 'she','his','--','mr','told',
    '-','mr.','were','had','how','while','said','had','many','its','i','my'
    ,'an','who','about','would', 'so','which','says','when', 'just','us','want'
    ,'more','get','use','some','than','then','made',"didn't",'into',
    'because','such','into','come','new','if','these','all','one',
    'two','me','him','go','me'}
    word_list = input_text.split(" ")
    for iw in irrelevant_words:
        for j in range(len(word_list)):
            if word_list[j] == iw:
                word_list[j] = ""
    return word_list


def histogram(word_list):
    """
    Return histogram for each file that have 
    the words and it repetitions
    """
    word_histogram = {}
    for word in word_list:
       if word not in word_histogram.keys():
           word_histogram[word] = 1
       else:
           word_histogram[word] = word_histogram[word] + 1
    word_histogram.pop("")
    return word_histogram


def article_keyword(my_dict):
    """
    Return at least three keyword for the articles
    """
    x=list(my_dict.values())
    x.sort(reverse=True)
    #Get rid of the number that repeats
    x=x[:3] 
    x = [*set(x)]
    keywords = []
    for i in x:
        for j in my_dict.keys():
            if(my_dict[j]==i):
                keywords.append(j)
    return keywords


def words_overlap_counter(keyword1,keyword2,file):
    """
    Take two diffrent keywords from diffrent articles
    Return number of overlap words
    """
    counter =0
    for i in range(len(keyword1)):
        for j in range(len(keyword2)):
            if keyword1[i] == keyword2[j]:
                counter = counter+1
    return [counter,file]


def the_most_intersection(keyword,keyword_list,files):  
    """
    compute the max number of overlap word for all articles 
    and return all the article have the max value overlap
    """
    articles_overlap =[]
    for i in range(len(keyword_list)):
        number_overlap_word = words_overlap_counter(keyword,keyword_list[i],files[i])
        # print(number_overlap_word[0])
        articles_overlap.append(number_overlap_word)
    
    relative_article_name =set()
    overlap_max_number = max(articles_overlap)
    if overlap_max_number[0] == 0: #no overlap words
        return("no relative article!!!!")      
    else:
        for i in range(len(articles_overlap)):
            if overlap_max_number[0] == articles_overlap[i][0]:
                relative_article_name.add(articles_overlap[i][1]) 
        return relative_article_name


def main_article(list_of_article,keywords):
    """
    return main article name and its keywords
    """
    print(*list_of_article, sep = "\n")    
    main_article_number = int(input("Enter the number of article you want to find it relevants \n"))
    main_article_keyword = keywords[main_article_number-1]
    main_article_name = list_of_article[main_article_number-1]
    keywords.remove(main_article_keyword)
    list_of_article.remove(main_article_name)
    return main_article_name,main_article_keyword
    
        
def main():
    list_of_article = article_name_list()
    keywords = []
    # this loop read the files and extract the keywords
    for i in range(len(list_of_article)):
        article_text = read_file(list_of_article[i])
        article_dictionary = histogram(word_lists(article_text))
        keyword = article_keyword(article_dictionary)
        keywords.append(keyword)
  
    main_article_name,main_article_keyword = main_article(list_of_article,keywords)

    print("Articles with the most intersection for",main_article_name)
    revalent = the_most_intersection(main_article_keyword,keywords,list_of_article)
    print(*revalent, sep = "\n")  
    
   
main()  

 






        
   
    
      



    


    

 