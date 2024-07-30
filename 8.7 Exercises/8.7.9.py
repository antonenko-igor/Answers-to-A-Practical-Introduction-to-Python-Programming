from random import sample

Questions = ["The capital of the Russian Federation ",
             "State in the USA has only one neighbor ",
             'The first man in space ',
             'The kind of precious metal is yellow ',
             'The second most important city in Russia ',
             'The river divides Orsk into Europe and Asia ',
             'The capital of the USA ',
             'The cold pole in Russia ',
             'The name of the monetary unit of Russia ',
             'The capital of France ']
Answers = ['Moscow','Maine','Gagarin','Golden','Saint-Petersburg','Ural',\
'Washington','Oymyakon','Rubel','Paris']
c = 0
L = []
s =sample(Questions,4)
for j in range(len(s)):
    x = Questions.index(s[j])
    L.append(Answers[x])
for i in range(len(s)):
    answer = input(s[i])
    if answer == L[i]:
        c = с + 1
        print("Right")
    else:
        print("Wrong")
print("Total correct answers:  ",c)  