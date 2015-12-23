def odds(iterable):
  odd_index_iterable = []
  index = 0
  while  index <= (len(list(iterable)) - 1):
    if index % 2 != 0 :
      odd_index_iterable.append(iterable[index])
    index += 1
  return (odd_index_iterable)
  
print(''.join(odds('Oklahoma')))

def first_and_last_4(iterable):
  copy_iterable = iterable[:]
  first_four = list(iterable[:4])
  last_four = list(copy_iterable[-4:])
  first_four.extend(last_four)
  return first_four
  
print(first_and_last_4(list(range(0,700))))

def sillycase(arg_str) :
    arg_list = list(arg_str);
    max_index = int(round(len(arg_str)/2))
    arg_list[:max_index] = arg_str[:max_index].lower()
    arg_list[max_index:] = arg_str[max_index:].upper()
    return (''.join(arg_list))

print(sillycase('Treehouse'))

def members(my_dict,my_list):
  # var to hold count
  count = 0
  # iterate over the list and try to find out the corresponding values for
  # keys of the same name
  for item in my_list:
    try:
        if my_dict[item] != None:
          count +=1
    except KeyError:
      continue
  return count

print(members({'apples': 1, 'bananas': 2, 'coconuts': 3},['apples', 'coconuts', 'grapes', 'strawberries']))


# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(arg_sentence):
    word_list_in_sentence = arg_sentence.lower().split(' ')
    word_frequency_dict = {}
    for word in word_list_in_sentence:
        # find out of the word appears in the dict
        if word in word_frequency_dict:
            # if the word is already present increment the value
            word_frequency_dict[word] +=1
        else:
            # if the word is not found add the word to the dict and continue
            word_frequency_dict[word] = 1
            continue;
    return word_frequency_dict
print(word_count('I am what i am'))



def most_classes(dict_teachers):
  teacher_name = None
  max_classes = 0
  for teacher in dict_teachers:
    # iterate over the dictionary
    # use the key to get the value
    if len(dict_teachers[teacher]) > max_classes:
      max_classes = len(dict_teachers[teacher])
      teacher_name = teacher
    else:
      continue
  return teacher_name
  
print(most_classes(  {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']}))


def stats(dict_teachers):
  list_teacher = []
  for teacher in dict_teachers:
    list_teacher_class = []
    list_teacher_class.append(teacher)
    list_teacher_class.append(len(dict_teachers[teacher]))
    list_teacher.append(list_teacher_class)
  
  return list_teacher
  
print(stats(  {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']}))

def combo(itr1,itr2):
  list_of_tupples = []
  for index , item in enumerate(itr1):
    list_of_tupples.append((index,itr2[index]))
  return list_of_tupples
  
  
print(combo([1, 2, 3], 'abc'))









