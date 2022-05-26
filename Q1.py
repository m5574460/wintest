
def twoSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        if str(target-nums[i]) not in dic:
            dic[str(nums[i])] = i
        else:
            return [dic[str(target-nums[i])], i]

def romanToInt(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
        else:
            num+=roman[s[i]]
            i+=1
    return num

# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3,2,4], 6))

# print(romanToInt("III"))
# print(romanToInt("CDXLIII"))
