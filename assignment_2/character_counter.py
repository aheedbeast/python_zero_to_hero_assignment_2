word_input = str(input ("enter any word to count its letters: "))

temp_store = list()

for i in word_input:
    if i not in temp_store:
        temp_store.append(i)
        print(f"{i}: count= {word_input.count(i)} ")