import unittest
from typesafelist import TypeSafeList

class TestStringMethods(unittest.TestCase):
	def test_init(self):
		fruit = TypeSafeList(["apple", "banana"])
		self.assertEqual(fruit, ["apple", "banana"])

	def test_modify(self):
		fruit = TypeSafeList(["apple", "banana"])
		fruit[1] = "strawberry"

		self.assertEqual(fruit, ["apple", "strawberry"])

		with self.assertRaises(TypeError):
			fruit.append("potato")

	def test_append(self):
		animals = TypeSafeList(["cat", "dog"])
		animals.append("elephant")

		self.assertEqual(animals, ["cat", "dog", "elephant"])

		with self.assertRaises(TypeError):
			animals.append("leaf")

	def test_insert(self):
		colors = TypeSafeList(["red", "blue"])
		colors.insert(1, "green")

		self.assertEqual(colors, ["red", "green", "blue"])

		with self.assertRaises(TypeError):
			colors.insert(2, "chair")

	def test_extend(self):
		directions = TypeSafeList(["north", "south"])
		directions.extend(["east", "west"])

		self.assertEqual(directions, ["north", "south", "east", "west"])

		with self.assertRaises(TypeError):
			directions.extend(["socks"])

if __name__ == '__main__':
	unittest.main()