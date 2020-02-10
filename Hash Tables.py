def first_hash(key, arrlen) :
    total = 0
    for char in key.lower() :
        val = ord(char) - 96
        total = (total + val) % arrlen
    return total
    
first_hash("cyan", 10)
