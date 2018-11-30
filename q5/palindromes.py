def palind(word):
    if ' ' in word:
        word_list = word.split()
        len_first = len(word_list[0])
        for token in word_list:
            token_len = len(token)
        new_word = ''.join(word_list)
        new_str = new_word[::-1]
        new_str = new_str[:len_first] + " " + new_str[len_first:]
        return new_str

    else:
        return word[::-1]

ans = palind("lesss sel")
