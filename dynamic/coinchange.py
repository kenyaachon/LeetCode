
"""
input: array of ints
amount: target


return the fewest number of coins that you need to make up the amount

if the amount can not be made by any combinations return -1

0
if there is no zero in the list
    return -1
    

[1, 2, 5] amount = 11

[5, 2, 1]

assumption the list is sorted
>sort the list
starting with the biggest coin

if I going to keep adding this denomiation of coin until, 
    the total is less than or equal to the amount
    if it becomes to big,
        then switch to the next the denomination
        
        
while iterating throught the coins, while still in range
    if I current coin + total less than or equal to amount
        then increment the number of coins used
        add coin to the total
        if coint + total == amount
            break
    else
        move to the next denomination
        
if the total == amount
    return number of coins used
return -1

time complexity of the algo O(n)*logn
    
amount = 51
[5, 2, 1]

amount = 12
[5, 3, 2, 1]
total = 0, 5, 10, 12 
number = 1, 2, 
5 + 5 + 2

amount = 3
[2]

2
number of coins is 1
-1



[186,419,83,408]

419, 408, 186, 

find all the combinations of coins from this array
    > look for the combinations that are equal to the amount
      > look for the one that has the smallesst number of coins used

"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #number of coins
        number = 0
        total = 0
        
        
        coins.sort(reverse=True)
        print(coins)
        i = 0
        #iterate through the array
        while (i < len(coins)):
            if total + coins[i] <= amount:
                number += 1
                total += coins[i]
                if total == amount:
                    break
            else:
                i += 1
        
        #check if the amount was acheived
        print(number)
        print(total)
        if total == amount:
            return number
    
        return -1

solution = Solution()
print(f"amount {11} coins {[1, 2, 5]} expected 3")
print(f"actual number {solution.coinChange([1, 2, 5], 11)}")
    

print(f"amount {3} coins {[2]} expected -1")
print(f"actual number {solution.coinChange([2], 3)}")  


print(f"amount {6249} coins {[186,419,83,408]} expected 20")
print(f"actual number {solution.coinChange([186,419,83,408], 6249)}")  
