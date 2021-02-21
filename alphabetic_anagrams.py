from math import factorial as f
from functools import reduce

# question
# [einoqstu]
# pos = 4*f(7) + 6*f(6) + 0*f(5) + 3*f(4) + 3*f(3) + 0*f(2) + 1*f(1) + 1
# print(pos)

# 4! / 4 + 4! / 2
# 3 * 4! / 4
# BEKKOO
# BEKOKO
# BEKOOK
# BEOKKO
# BEOKOK
# BEOOKK
# BKEKOO
# BKEOKO
# BKEOOK
# BKKEOO
# BKKOEO
# BKKOOE
# BKOEKO
# BKOEOK
# BKOKEO
# BKOKOE
# BKOOEK
# BKOOKE
# BOEKKO
# BOEKOK
# BOEOKK
# BOKEKO
# BOKEOK
# BOKKEO
# BOKKOE
# BOKOEK
# BOKOKE
# BOOEKK
# BOOKEK
# BOOKKE



word = "IMMUNOELECTROPHORETICALLY"

def unique(word):
    return sorted(list(set(word)))

def non_unique_comb(word):
    if _print == True:
        print("finding non_unique_comb")
    non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
    
    if _print == True:
        print(f"word: {word}")
        print(f"non_unique_factorials: {non_unique_factorials}")
    return non_unique_factorials if non_unique_factorials else [1]

def non_unique_combs(word):
    if _print == True:
        print("finding non_unique_combs")
    output = list(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
    if _print == True:
        print(f"word: {word}")
        print(f"non_unique_combs: {output if output != 0 else 1}")
    return output 

def combs(word, i):
    combinations = 0
    print(f"non_unique_combs: {non_unique_combs(word[i:])}")
    for factorials in non_unique_combs(word[i:]):
        factors = list(range(1, len(word) - i))
        print(f"factorials = {factorials}")
        for k in range(len(factors)):
            if set(factorials) == {float("inf")}:
                break  
            for j in range(len(factorials)): 
                if factors[k] % factorials[j] == 0:
                    factors[k] = int(factors[k] / factorials[j])
                    factorials[j] = float("inf")
        print(f"factors = {factors}")
        print(f"factorials = {factorials}")
        factors = [int(n) for n in factors]
        print(f"combination = {int(reduce((lambda a,b: a * b), factors))}")
        combinations += int(reduce((lambda a,b: a * b), factors))
    print(f"combinations: {combinations}")
    return combinations


# def combs(word, i):
#     print(f"combs: {sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  )}")
#     return sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  )


_print = True
print(sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1)

# RESULT WITH AVOIDING DIVIDING LARGE NUMBERS
# combinations: 628347629070120960000
# combinations: 82283618092515840000
# combinations: 7155097225436160000
# combinations: 591330349209600000
# combinations: 15487223431680000
# combinations: 774361171584000
# combinations: 33345696384000
# combinations: 12967770816000
# combinations: 980755776000
# combinations: 40864824000
# combinations: 65383718400
# combinations: 7783776000
# combinations: 838252800
# combinations: 39916800 #WRONG 
# combinations: 5443200 
# combinations: 362880 #WRONG
# combinations: 40320 SHOULD EQUAL 120960
# combinations: 5040
# combinations: 720 # WRONG
# combinations: 120
# combinations: 12
# 718393983731025140293

# RESULT WITH DIVIDING LARGE NUMBERS
# combs: 628347629070120976384
# combs: 82283618092515840000
# combs: 7155097225436160000
# combs: 591330349209600000
# combs: 15487223431680000
# combs: 774361171584000
# combs: 33345696384000
# combs: 12967770816000
# combs: 980755776000
# combs: 40864824000
# combs: 65383718400
# combs: 7783776000
# combs: 838252800
# combs: 159667200
# combs: 5443200
# combs: 1088640
# combs: 120960
# combs: 5040
# combs: 1800
# combs: 120
# combs: 12
# 718393983731145714557


# SECOND VERSION FOR CODEWARS

# def unique(word):
#     return sorted(list(set(word)))

# def non_unique_comb(word):
#     non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
#     return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 1

# def non_unique_combs(word):
#     output = list(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
#     return output if sum(output) != 0 else [1]

# def combs(word, i):
#     return sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  )
 
# return sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1





# FIRST SOLUTION THAT WORKED FOR "QUESTION"

# def listPosition(word):
#     from math import factorial as f
#     from functools import reduce
    
#     def unique(word):
#         return sorted(list(set(word)))

#     def non_unique_comb(word):
#         non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
#         return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 0
    
#     def non_unique_combs(word):
#         output = sum(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
#         return output if output != 0 else 1
        
#     return sum((unique(word[i:]).index(word[i]) * f(len(word) - i - 1)) / (non_unique_combs(word[i:])) for i in range(len(word)-1)) + 1



# 628347629070120976384
# 628347629070120960000

# finding non_unique_comb
# word: IMMUNOELECTROPHORETICLLY
# non_unique_factorials: [2, 6, 2, 6, 2, 6, 2, 2]
# finding non_unique_comb
# word: IMMUNOELETROPHORETICALLY
# non_unique_factorials: [6, 2, 6, 2, 6, 2, 2]
# finding non_unique_comb
# word: IMMUNOLECTROPHORETICALLY
# non_unique_factorials: [2, 2, 2, 6, 2, 6, 2, 2]
# finding non_unique_comb
# word: IMMUNOELECTROPORETICALLY
# non_unique_factorials: [2, 6, 2, 6, 2, 6, 2, 2]
# word: IMMUNOELECTROPHORETICALLY
# non_unique_combs: [6912, 3456, 2304, 6912]
# combs: 628347629070120976384


# PYTHON FAILING TO DIVIDE A LARGE NUMBER CORRECTLY
# >>> int(269291841030051856384/3)
# 89763947010017280000
# >>> 89763947010017280000 * 3
# 269291841030051840000

# factorials = [2, 2, 2, 6, 2, 6, 2, 2]
# factors = list(range(1,25))
# for i in range(len(factors)):
#     if set(factorials) == {float("inf")}:
#         break  
#     for j in range(len(factorials)):
#         print(f"factor: {factors[i]}")
#         print(f"factorial: {factorials[j]}")
#         if set(factorials) == {float("inf")}:
#             break   
#         if factors[i] % factorials[j] == 0:
#             print(f"{factors[i]} is div by {factorials[j]}")
#             factors[i] /= factorials[j]
#             factorials[j] = float("inf")
#             print(f"{factors}")
#             print(f"{factorials}")

# factors = [int(n) for n in factors]
# print(int(reduce((lambda a,b: a * b), factors)))
# print(int(reduce((lambda a,b: a * b), [1, 1.0, 3, 1.0, 5, 1.0, 7, 1.0, 9, 10, 11, 2.0, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])))

# del factors[2]
# print(int(reduce((lambda a,b: a * b), factors)))
# print(int(reduce((lambda a,b: a * b), list(range(1,25)))))



# BEFORE FIXING PYTHON DIVISION ISSUE

# word = "IMMUNOELECTROPHORETICALLY"

# def unique(word):
#     return sorted(list(set(word)))

# def non_unique_comb(word):
#     if _print == True:
#         print("finding non_unique_comb")
#     non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
    
#     if _print == True:
#         print(f"word: {word}")
#         print(f"non_unique_factorials: {non_unique_factorials}")
#     return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 1

# def non_unique_combs(word):
#     if _print == True:
#         print("finding non_unique_combs")
#     output = list(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
#     if _print == True:
#         print(f"word: {word}")
#         print(f"non_unique_combs: {output if output != 0 else 1}")
#     return output if sum(output) != 0 else [1]

# def combs(word, i):
#     print(f"combs: {int(sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  ))}")
#     return sum( map(  lambda comb: f(len(word) - i - 1) / comb,  non_unique_combs(word[i:]) )  )


# _print = False    
# print(int(sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1))



# BEFORE FIXING DIVISION ISSUE. COPIED FROM CODEWARS

# def unique(word):
#     return sorted(list(set(word)))

# def non_unique_comb(word):
#     non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
#     return reduce((lambda a, b: a * b), non_unique_factorials, 1) if non_unique_factorials else 1

# def non_unique_combs(word):
#     output = list(non_unique_comb(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))
#     return output if sum(output) != 0 else [1]

# def combs(word, i):
#     return sum(map(lambda comb: int(int(f(len(word) - i - 1)) / comb), non_unique_combs(word[i:])))
    
# for num in list(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]):
#     print(f"combs: {num}")
# print(sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1)



# #  FINAL ANSWER!!!!!!!!!!!

# def unique(word):
#     return sorted(list(set(word)))

# def repeated_let_combs(word):
#     non_unique_factorials = [f(word.count(unique(word)[i])) for i in range(len(unique(word))) if word.count(unique(word)[i]) > 1]
#     return non_unique_factorials if non_unique_factorials else [1]

# def all_repeated_let_combs(word):
#     return list(repeated_let_combs(word[:word.index(unique(word)[i])] + word[word.index(unique(word)[i])+1:]) for i in range(0,unique(word).index(word[0])))

# def combs(word, i):
#     combinations = 0
#     for factorials in all_repeated_let_combs(word[i:]):
#         factors = list(range(1, len(word) - i))
#         for k in range(len(factors)):
#             if set(factorials) == {float("inf")}:
#                 break  
#             for j in range(len(factorials)): 
#                 if factors[k] % factorials[j] == 0:
#                     factors[k] = int(factors[k] / factorials[j])
#                     factorials[j] = float("inf")
#         combinations += int(reduce((lambda a,b: a * b), factors))
#     return combinations

# return sum(combs(word,i) for i in range(len(word)-1) if word[i] != unique(word[i:])[0]) + 1