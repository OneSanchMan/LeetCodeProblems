class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        arr1 = sorted(seats)
        arr2 = sorted(students)
        return sum([abs(arr1[i]-arr2[i]) for i in range(len(seats))])