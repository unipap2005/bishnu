def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    k=0
    max_instances = 2*10^8
    length=len(averageUtil)
    for i in averageUtil:
        print(averageUtil[k])
        if averageUtil[k] < 25:
            if instances!=1:
                instances /=2
                if(averageUtil[k+10] < length):
                    k +=10
                else:break
            else:
                if(averageUtil[k+10] < length):
                    k +=1
                else:break
        elif averageUtil[k] in (25,60):
            if(averageUtil[k+10] < length):k+=1
            else:break
        elif averageUtil[k] > 60:
            if instances < max_instances/2 :
                instances *=2
                if(averageUtil[k+10] < length):
                    k +=10
                else:break
            else:
                if(averageUtil[k+10] < length):k+=1
                else:break
    print (instances)

finalInstances(2,[25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80])






