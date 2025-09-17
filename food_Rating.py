import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.rated_cuisine = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (rating, cuisine)
            self.rated_cuisine[cuisine].append((-rating, food))
        
        for cuisine in self.rated_cuisine:
            heapq.heapify(self.rated_cuisine[cuisine])


    def changeRating(self, food: str, newRating: int) -> None:
        _, curr_cuisine = self.foods[food]
        self.foods[food] = (newRating, curr_cuisine)
        heapq.heappush(self.rated_cuisine[curr_cuisine], (-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        while self.rated_cuisine[cuisine][0][0] != -self.foods[self.rated_cuisine[cuisine][0][1]][0]:
            heapq.heappop(self.rated_cuisine[cuisine])
        return self.rated_cuisine[cuisine][0][1]

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
