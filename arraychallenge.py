
arr = [1,2,2,3] # Working input from test
# arr = [0,0,0,0,1]

# arr = [0,2,1,1,1,1,1,1]

dbl_arr = []
for itm in arr:
    dbl_arr.append([itm,0])


for count, item in enumerate(dbl_arr):
    if count == 0:
        continue
    for back_count in range(0,count):
        print('count, bc: ',count,back_count)
        
        print(dbl_arr[count - back_count-1][0])
        print(dbl_arr[count][0])
        # if previous element is GTE current, then subtract the difference
        if dbl_arr[count - back_count-1][0] >= dbl_arr[count][0]:
            diff = (dbl_arr[count][0] - dbl_arr[count - back_count-1][0])
            print('GT, sub, diff is:', count, diff)
            dbl_arr[count][1] = dbl_arr[count][1] - diff
        # if previous element is LT current, then add the difference
        elif dbl_arr[count - back_count-1][0] < dbl_arr[count][0]:
            diff = (dbl_arr[count][0] - dbl_arr[count - back_count-1][0])
            print('LT, add, diff is:', diff)
            dbl_arr[count][1] = dbl_arr[count][1] + diff
            #dbl_arr[count][1] += (dbl_arr[count][0] + dbl_arr[count -1][0])
    print(dbl_arr,'\n')
    
ans = []
for item in dbl_arr:
    ans.append(item[1])

  
print('\nAns: ',ans)
