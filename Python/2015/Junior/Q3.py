abc = ["a", "b", "c", "d" ,"e" ,"f","g", "h" ,"i", "j", "k", "l", "m" ,"n" ,"o" ,"p" ,"q" ,"r","s" ,"t", "u", "v", "w", "x", "y","z"]
vowels = ["a","e","i","o","u"]
a_e = ["a", "b", "c", "d" ,"e"]
e_i = ["e" ,"f","g", "h" ,"i"]
i_o = ["i", "j", "k", "l", "m" ,"n" ,"o"]
o_u = ["o" ,"p" ,"q" ,"r","s" ,"t", "u"]
line = list(input()) 
new_word = []
for letter in line:
    if letter in vowels:
        new_word.append(letter)
        continue
    new_word.append(letter)
    if letter in a_e:
        a_closer = a_e.index(letter) - 0
        e_closer = 4 - a_e.index(letter)
        if a_closer < e_closer or a_closer == e_closer:
            new_word.append("a")
        elif e_closer < a_closer:
            new_word.append("e")
    elif letter in e_i:
        e_closer = e_i.index(letter) - 0
        i_closer = 4 - e_i.index(letter)
        if e_closer < i_closer or e_closer == i_closer:
            new_word.append("e")
        elif i_closer < e_closer:
            new_word.append("i")
    elif letter in i_o:
        i_closer = i_o.index(letter) - 0
        o_closer = 6 - i_o.index(letter)
        if i_closer < o_closer or i_closer == o_closer:
            new_word.append("i")
        elif o_closer < i_closer:
            new_word.append("o")
    elif letter in o_u:
        o_closer = o_u.index(letter) - 0
        u_closer = 6 - o_u.index(letter)
        if o_closer < u_closer or o_closer == u_closer:
            new_word.append("o")
        elif u_closer < o_closer:
            new_word.append("u")
    else:
        new_word.append("u")
    if letter == "z":
        new_word.append("z")
    elif abc[abc.index(letter)+1] in vowels:
        new_word.append(abc[abc.index(letter)+2])
    else:
        new_word.append(abc[abc.index(letter)+1])

print("".join(new_word))