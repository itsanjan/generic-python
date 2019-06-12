list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
list2 = [[1,5,9],[2,6,10],[3,7,11],[4,8,12]]

def inverse(list):
    for m in range (0,len(list)):
        for n in range (0,len(list[m])):
            print(list[m][n])

if '__info__'=='__main__':
    inverse(list1)