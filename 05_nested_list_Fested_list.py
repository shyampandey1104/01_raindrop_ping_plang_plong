def flat(lis):
    
    flatList = []

    

    for element in lis:

        if type(element) is list:

            

            for item in element:
                if item == "nil" or item == "null":
                    pass
                else:
                    flatList.append(item)

        else:
            flatList.append(element)

    return flatList

test = [1,[2,3,"null",4],["null"],5]
print(flat(test))
