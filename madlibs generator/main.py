

with open("D:/Codes/projects/madlibs generator/story.txt","r") as f:
    story = f.read()

#words = [] #using set because it does not allow to add same data name our list
words = set()

lst_words = []

start_of_words = -1

target_start = '<'
target_end = '>'

for i,char in enumerate(story): #(enumerate) gives us the word and the intentation of the word
    if char == target_start:
        start_of_words = i
    
    if char == target_end and start_of_words != -1:
        word = story[start_of_words:i+1]
        #============================
        lst_words.append(word)
        #============================
        words.add(word) #add for set() dataset
        start_of_words = -1

#=============================
unique_lst_words = list(dict.fromkeys(lst_words)) #in order to remove copy values just like set()
#============================
answers = {}

# print(unique_lst_words)
# print(words)

for i in words:
    user = input("Enter the word to replace with "+i+":")
    answers[i] = user

for word in words : 
    story = story.replace(word,answers[word])

print(story)