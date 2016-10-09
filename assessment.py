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

    test_type = 'exam'

    def __init__(self, name):
        """Initialize an exam"""

        self.questions = []
        self.name = name

    def add_question(self, question_string, answer_string):
        """Add a question to the exam"""

        self.questions.append(Question(question_string, answer_string))

    def administer(self):
        """Administers exam questions and returns user's score"""

        score = 0.0
        count = 0
        for question in self.questions:
            count += 1
            if Question.ask_and_evaluate(question):
                score += 1
        print score / count * 100, "%"
        return score / count * 100


class Quiz(Exam):
    """A quiz"""

    test_type = 'quiz'

    def administer(self):
        """Administers quiz questions and returns user's pass/fail status"""

        quiz_score = super(Quiz, self).administer()
        if quiz_score >= 50:
            print "Pass! :)"
            return "pass"
        else:
            print "Fail! :("
            return "fail"


def take_test(exam, student):
    """Administers a test and tracks student's score.

    Calls .adminster() method on an existing Exam() object, and assigns a new
    total score result as an instance attribute to an existing Student() object.
    """

    if type(exam) is Quiz:
        student.quiz_score = exam.administer()
    elif type(exam) is Exam:
        student.exam_score = exam.administer()


def example():
    """Example setup to create and take an exam.

    Initializes new Exam() object, adds 3 questions to it with their associated
    correct answers. Initializes a Student() object. Calls take_test function on
    the new exam and new student, requiring user input for each questions, and
    prints the score results to the console.

    ***NOTE*** the take_test function when called directly in the console does
    successfully add a student.score attribute value to an existing Student()
    object. Because this example is called entirely within a function, student
    attributes will not be saved once the example function completes.
    """

    exam1 = Exam('midterm')
    exam1.add_question('What is the method for adding an element to a set?', '.add()')
    exam1.add_question('what is my favorite color?', 'purple')
    exam1.add_question('what is 2 + 2?', '4')

    a_student = Student("jen", "b", "123 sesame st")

    take_test(exam1, a_student)

example()


## objects instantiated outside of example() function for interactive console
## testing purposes:
exam1 = Exam('midterm')
exam1.add_question('What is the method for adding an element to a set?', '.add()')
exam1.add_question('what is my favorite color?', 'purple')
exam1.add_question('what is 2 + 2?', '4')

a_student = Student("jen", "b", "123 sesame st")

quiz1 = Quiz('quiz1')
quiz1.add_question('What are three benefits of OO?', 'abstraction, encapsulation, and polymorphism')
quiz1.add_question('How many pets do I have?', '1')
quiz1.add_question('Raven?', 'CAWW!')

"""Example output (not in a DocString test because I don't know how to simulate
    raw input):

    >>> type(quiz1)
    <class '__main__.Quiz'>
    >>> type(exam1)
    <class '__main__.Exam'>
    >>> len(quiz1.questions)
    3
    >>> len(exam1.questions)
    3
    >>> quiz1.questions[2].answer
    'CAWW!'
    >>> exam1.questions[1].question
    'what is my favorite color?'
    >>> take_test(quiz1, a_student)
    What are three benefits of OO? > abstraction, encapsulation, and polymorphism
    How many pets do I have? > 1
    Raven? > CAWW!
    100.0 %
    Pass! :)
    >>> a_student.quiz_score
    'pass'
    >>> a_student.exam_score
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'Student' object has no attribute 'exam_score'
    >>> take_test(exam1, a_student)
    What is the method for adding an element to a set? > .add()
    what is my favorite color? > purple
    what is 2 + 2? > 3
    66.6666666667 %
    >>> a_student.exam_score
    66.66666666666666
    >>> a_student.quiz_score
    'pass'

"""
