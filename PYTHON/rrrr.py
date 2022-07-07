def reverseString(s):
    list1 = []
    string = ' '
    i = 0
    l = len(s)
    for item in s:
        if item !=' ':
            string +=item
            i+=1
            continue
        if item == ' ':
            # string+=' '
            list1.append(string)
            string = ' '
            i+=1
    list1.append(string)
    for i in range(len(list1)):
        ans = ''.join(reversed(list1[i]))
        list1[i] = ans
    print(list1)
    return ''.join(list1)


print(reverseString( "Let's take LeetCode contest"))