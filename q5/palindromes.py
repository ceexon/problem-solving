def palind(word):
    if ' ' in word:
        word_list = word.split()
        len_first = len(word_list[0])
        new_word = ''.join(word_list)
        new_str = new_word[::-1]
        new_str = new_str[:len_first] + " " + new_str[len_first:]
        return new_str

    else:
        return word[::-1]

ans = palind("lesss sel")
ans1 = palind("nurses run")

print (ans)
print (ans1)
