new_list = [1, 'DIDIER', 'Joe', 'Tito', 3, 3, 'johnny', 3, 'Peter', 1, 'DIDIER', 5, 1 , 'Joe', ['Tito', 5, 1]]

length = len(new_list)
#print(length)
while length > 0:
    for x in range(length):
        #exit if index greater than size
        if x >= len(new_list):
            break
        else: 
            if new_list.count(new_list[x]) > 1:
                count = new_list.count(new_list[x])
                value = new_list[x]
                for i in range(count):
                    new_list.remove(value)
        length = length -1
print(new_list)
