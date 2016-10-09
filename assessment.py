"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.



2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


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
