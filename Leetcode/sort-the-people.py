class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key=lambda x: x[1], reverse=True)
        return [i[0] for i in people]
