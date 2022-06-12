class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # max_sum=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         sub_array=nums[i:j]
        #         print(sub_array)
        #         if(sorted(list(set(sub_array)))==sorted(sub_array)):
        #             temp_sum=sum(sub_array)
        #             if(temp_sum>max_sum):
        #                 max_sum=temp_sum
        # return max_sum
        # arr=[]
        # currSum=0
        # maxSum=0
        # for i in range(len(nums)):
        #     if (nums[i] not in arr):
        #         arr.append(nums[i])
        #         currSum+=nums[i]
        #         if (currSum>maxSum):
        #             maxSum=currSum
        #     else:
        #         index = arr.index(nums[i])
        #         arr = arr[index+1:]
        #         arr.append(nums[i])
        #         currSum = sum(arr)
        #         if(currSum>maxSum):
        #             maxSum = currSum
        # return maxSum
        
        win, curr_sum = set(), 0 #windows element and it's sum
        ans = 0 # maximum val
        st = 0 # starting index
        for num in nums:
            if num not in win: # if unique than add
                win.add(num)
                curr_sum += num
            else:
                while num in win: # remove all element untill window has not unique val
                    win.discard(nums[st])
                    curr_sum -= nums[st]
                    st += 1
                win.add(num) #after removing all duplicate add current val
                curr_sum += num
            ans = max(ans,curr_sum) # taking max value
        return ans
                
            