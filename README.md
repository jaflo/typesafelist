# TypeSafeList

`TypeSafeList` makes sure that your lists of strings remain type-safe by rejecting invalid strings from inappropriately-named lists.

Requires the [Natural Language Toolkit (NTLK)](https://www.nltk.org/) to be installed.

## Example

After importing the package you will need to convert your regular list to a `TypeSafeList` which retains the behavior of a normal list but provides additional type safety:

```
from typesafelist import TypeSafeList

fruit = TypeSafeList(["apple", "banana"])
fruit[1] = "onion" # TypeError: onion must be fruit
```

## Implementation

On each insertion or update, NLTK is used to determine the hypernyms (read categories) of the value to be inserted and checked against the variable name to see if the operation is valid. If it isn't, a `TypeError` is raised.

## Limitations

* Currently only supports storing strings (no image classification yet).
* Slows down your program a *lot* (~1s/op).
* Does not check entries that already existed prior to conversion.
* Does not protect against renaming of the list.
* Supports English only.

## Disclaimer

Please never use this in production, someone will cry. This is a joke (implemented using awful and hacky Python code) insprired by [this post](https://www.reddit.com/r/ProgrammerHumor/comments/ad6knh/actual_question_on_my_mock_exam/).
