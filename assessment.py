"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Object-oriented programming provides three primary design advantages in the form
of the following:
    Abstraction is the idea of hiding or obscuring details that aren't necessary
        for an end user to utilize a given set of functions or methods. All
        that's necessary is that the user understands how to use a function or
        method, without necessarily understanding how/why it works.
    Encapsulation is the idea of keeping pieces of data close to the functions/
        methods/classes that use them. For example, all pieces of data relevant
        to a Cat() class such as meowing & purring would be enclosed within that
        class and/or limited my methods defined only within that class.
    Polymorphism is the idea of interchangeability of components. In other
        words: "when a method or function is able to cope with different types
        of input." (http://stackoverflow.com/a/3322677) Polymorphism is
        dependent on abstraction & encapsulation; it is this encapsulation that
        facilitates a function or method's ability to handle these different
        types of input.

2. What is a class?

    A class is a type of object; a way to define a type of thing in Python. At
    its most basic level, a given custom defined class will always be a subclass
    to the more general class of Objects.

3. What is an instance attribute?

    Classes can have attributes, whether self-defined or inherited. These
    attributes are generally shared by all members of this class. Since an
    instance is an example of an instantiated object for a given class type,
    instance attributes are that instance's actual values for a given attribute.
    For example, if an Animal() class has an attribute self.species, an instance
    of that class could have the instance attribute value of 'dog.'

4. What is a method?

    A method is like a function defined within a class, that is only accessible
    (i.e. can be run by) to instances that are members of that class and/or
    its subclasses.

5. What is an instance in object orientation?

    In object orientation, an instance is a real/defined object in memory or in
    in the program that is a member of a defined class. Classes can be defined,
    but cannot directly be manipulated or acted upon in some way. Instead this
    applies to the instance object of that class. Cats exist as an intangible
    class of the idea of felines, but my own cat is a real, existing instance
    object of that class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is one that, by design, is generally shared by all members
   of a class, whereas an instance attribute is one that pertains specifically
   to an instance object in that class. When defining a class of Dogs() it could
   be helpful to define a class attribute for all hypothetical members of this
   class where self.species = 'dog.' If Fido is instantiated by fido = Dogs()
   and self.name is set to 'Fido', the value of 'Fido' here represents an
   instance attribute. Similarly, overwriting self.species to = 'terrier' would
   also represent an instance attribute pertaining solely to 'fido.'


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A student"""

    def __init__(self, first, last, address):
        """Initialize a student."""

        self.first_name = first
        self.last_name = last
        self.address = address


class Question(object):
    """A question and it's correct answer.

    """

    def __init__(self, question_string, answer_string):
        """Initialize a question-answer pair."""

        self.question = question_string
        self.answer = answer_string

    def ask_and_evaluate(self):
        print self.question,
        guess = raw_input("> ")
        if guess == self.answer:
            return True


class Exam(Question):
    """An exam"""

    def __init__(self, name):
        """Initialize an exam"""

        self.questions = []
        self.name = name

    def add_question(self, question_string, answer_string):
        """Add a question to the exam"""

        self.questions.append(Question(question_string, answer_string))

    def administer(self):
        """Administers exam questions and returns user's score"""

        score = float(0.0)
        for question in self.questions:
            reply = Question.ask_and_evaluate(question)
            if reply is True:
                score += 1
        print score


## testing purposes, to be removed later
exam = Exam('midterm')
question = Question('What is the method for adding an element to a set?', '.add()')
exam.add_question('What is the method for adding an element to a set?', '.add()')
