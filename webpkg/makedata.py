def adddatas(keylist, valuelist):

    count = 0

    # Save keylists
    for key in keylist:
        result = {key: ""} # key:value
        if len(keylist) == count:
            break
        else:
            count += 1

    count = 0
    # Save valuelists
    for value in valuelist:
        result[keylist[count]] = value
        if len(valuelist) == count:
            break
        else:
            count += 1

    # Check saved result value
    # print(result)
    return result