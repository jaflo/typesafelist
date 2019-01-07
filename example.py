from typesafelist import TypeSafeList

fruit = TypeSafeList(["apple", "banana"])

fruit[1] = "strawberry"
print(fruit)

fruit.append("onion") # TypeError: onion must be fruit
