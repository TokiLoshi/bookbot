def main():
  book_to_read = "books/frankenstein.txt"
  print(f"--- Begin report of {book_to_read} ---")
  with open(book_to_read) as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")

    # Sort characters to report 
    character_count = count_characters(file_contents)
    dictionary_list = [character_count]
    sorted_dictionary = sort_dictionary(character_count)
    
    # Report sorted characters
    for character in sorted_dictionary:
      if character["character"].isalpha():
        print(f"The {character["character"]} character was found {character["number"]} times")

    print("--- End of book report ---")

def sort_dictionary(dictionary):
  list_to_sort = []
  for character in dictionary: 
    list_to_sort.append({"character": character, "number": dictionary[character]})
  list_to_sort.sort(reverse=True, key=sort_on)
  return list_to_sort

def sort_on(dict):
  return dict["number"]

def count_words(words):
  words = words.split()
  word_count = len(words)
  return word_count

def count_characters(words):
  character_frequency = {}
  for word in words:
    lowercase_word = word.lower()
    characters = lowercase_word.split()
    for char in characters: 
      if char in character_frequency:
        character_frequency[char] += 1
      else: 
        character_frequency[char] = 1
  return character_frequency

main()

