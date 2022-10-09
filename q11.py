def histrogram(nums):
    for x in nums:
        output = ''
        while x > 2:
            output = output + "x"
            x = x - 2
        print(output)
histrogram([66 , 7 , 8 , 9 , 7] )