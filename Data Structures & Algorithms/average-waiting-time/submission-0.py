class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        total_wait = 0
        for arrival,cook_time in customers:
            start_time =max(curr_time,arrival)
            curr_time = start_time+cook_time
            total_wait += curr_time - arrival

        avg = total_wait/(len(customers))
        return avg
            





        