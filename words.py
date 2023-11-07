from random_word import RandomWords


one_random_word = RandomWords()
# for _ in range(5):
#     print(one_random_word.get_random_word())

list_of_random_words = [one_random_word.get_random_word().upper() for _ in range(5)]
sorted_list_of_random_words = sorted(list_of_random_words)
print(sorted_list_of_random_words)