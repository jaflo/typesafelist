import inspect
from nltk.corpus import wordnet as wn

class TypeSafeList(list):
	def __init__(self, *args, **kwargs):
		if len(args) > 0:
			super(TypeSafeList, self).__init__(args[0])
		else:
			super(TypeSafeList, self).__init__()

	def __setitem__(self, key, value):
		if self.is_valid(value, raise_error=True):
			super(TypeSafeList, self).__setitem__(key, value)

	def append(self, value):
		if self.is_valid(value, raise_error=True):
			super(TypeSafeList, self).append(value)

	def insert(self, i, value):
		if self.is_valid(value, raise_error=True):
			super(TypeSafeList, self).insert(i, value)

	def extend(self, values):
		for value in values:
			if not self.is_valid(value, raise_error=True):
				pass # a error will be raised, we will never get here
		super(TypeSafeList, self).extend(values)

	def is_valid(self, value, raise_error=False):
		# find name of variable (self), https://stackoverflow.com/a/18425275
		callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
		names = [var_name for var_name, var_val in callers_local_vars if var_val is self]

		try:
			valid_categories = wn.synsets(value)
		except LookupError:
			import nltk
			nltk.download("wordnet")

		# find categories this could belong to, https://stackoverflow.com/a/26227542
		valid_categories = [category.closure(lambda s:s.hypernyms()) for category in valid_categories]
		# flatten and make unique, https://stackoverflow.com/a/952952
		valid_categories = set([item for sublist in valid_categories for item in sublist])

		actual_categories = [wn.synsets(name) for name in names]
		actual_categories = set([item for sublist in actual_categories for item in sublist])

		# check if any categories match
		valid = not actual_categories.isdisjoint(valid_categories)

		if not valid and raise_error:
			if len(names) == 1:
				raise TypeError("%s must be %s" % (value, names[0]))
			else:
				raise TypeError("%s must be one of %s" % (value, ", ".join(names)))

		return valid
