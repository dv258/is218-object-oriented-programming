# Explaining Object-Oriented Programming With Python
[![Build Status](https://travis-ci.org/dv258/is218-object-oriented-programming.svg?branch=master)](https://travis-ci.org/dv258/is218-object-oriented-programming)

The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism.

## Encapsulation
The principle of encapsulation is to keep properties belonging to an object private from other external objects. Private properties are only interactable through the public class methods. For instance, a car object may have a private variable that stores the license plate number. Encapsulation would ensure that there is a public method to get the license plate number, but would likely not have a public function to set the license plate number. This prevents any external objects from changing the license plate value. This also has the benefit of having the license plate number publicly retrievable from only one public function, which helps funnel code and increases readability. This example can be found in [encapsulation.py](./encapsulation.py).

## Abstraction
Abstraction is the concept of providing objects with high-level interfaces to perform certain tasks, without the caller knowing what the internal implementation looks like. This allows the internal code to change as needed, as long as it still performs the same actions the high-level caller expects it to. An example can be demonstrated with a Library class that is designed to hold a collection of books. The Library class has public functions to find and checkout books, but the caller of those functions does not need to know how they work. In fact, the algorithm for finding books in the Library may be changed or optimized without the knowledge of the caller, and the caller would not be negatively affected since it is only dealing with the high-level interface supplied by the Library class. An example of abstraction can be found in [abstraction.py](./abstraction.py).

## Inheritance
Having classes that extend or expand upon functions from other classes is called inheritance. Inheritance is useful for objects that share similar properties to one another, but behave in some different ways. A cat and dog, for example, are similar in that they both eat and sleep, but one of them meows, while the other barks. They both can be seen as subsets of a greater collection, like an animal, and extend of off it. Using inheritance allows the Cat and Dog class to share similar code, but also allows them to have their own code that is specifically related to them. The example can be found in [inheritance_polymorphism.py](./inheritance_polymorphism.py).

## Polymorhpism
The concept of polymorphism is to use similar, but differently typed, objects as if they were the same and perform actions that can be applied to the set of similar objects. Using the example above, a function may take in an Animal class and call a function called *noise*. Depending on what type the animal passed in is, the *noise* function will return a different noise. If a cat was passed to *noise*, it would return "meow", whereas if a dog was passed, the function would return "woof".
