for x in range(32,54):
    for y in range(46,68):
        for z in range(116,318):
            if x + y  ==  z:
                X = [32,34,52,54] # difference per unit from 43
                Y = [46,48,66,68] # difference per unit from 57
                if x in X and y in Y:
                    print("x = ",x, "; y = ",y,"; z = ",z) 