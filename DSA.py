class Solution:
 
    def mergeSort(self, arr, l, r):
        if len(arr)<=1: # if length < 1
            return arr
        mid= len(arr)//2 # this so mid
        left_arr= arr[:mid]
        right_arr= arr[mid:]
        left_arr= self.mergeSort(left_arr, l ,r)
        right_arr= self.mergeSort(right_arr,l , r)
        return self.merge_arr(left_arr,right_arr)
        
        
    
        
    def merge_arr(self, l,r):
        i=0
        j=0
        empty=[]
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                empty.append(l[i])
                i+=1
            else:
                empty.append(r[j])
                j+=1
                
        empty.extend(l[i:])
        empty.extend(r[j:])
        return empty        
    
arr= [8,4,5,6,7,263,784,2]        
sol = Solution()
print(sol.mergeSort(arr, None, None))
