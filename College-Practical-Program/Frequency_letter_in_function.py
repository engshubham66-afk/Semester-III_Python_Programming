def frequency_letter():
    sentence = input("Enter sentence: ")
    freq = {}
    
    for ch in sentence:
        if ch != " ":
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch]  = 1
        
    print("Frequency of each letter: ", freq)

frequency_letter()    