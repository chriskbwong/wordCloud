import re

def word_split(file):
  words = re.split("[\n (.)+]",file)
  word_cloud = {}
  for word in words:
    word = re.sub("[,;:'.?(')()!&$]", "", word).lower()
    if word in word_cloud.keys():
      word_cloud[word] += 1
    else:
      word_cloud[word] = 1
  print (word_cloud)
  
input_sentence = """After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar."""
word_split(input_sentence)
