
'''Weekend assignment:
Create a python abstract class called Shape with abstract methods for calculating the area and perimeter of shapes. 
Then create the subclasses rclTriangle, Cie, Square from the Shape class and implement their respective area and perimeter methods.
Each Shape subclass should upon instantiation, receive their individually required attributes that would be useful in eventually calculating their areas and perimeters.
However, before implementing these classes, endeavour to write unittests for each subclass and their methods. 
 
Acceptance Criteria:
Code includes a class named Shape
Code includes a class named Triangle
Code includes a class named Circle
Code includes a class named Square
Each of the aforementioned classes must contain at least two methods which shall be named area and perimeter.
There should be at least three test classes: one for each shape subclass. The test classes must contain at least 12 testcases each. 
- At least 6 tests for the area method, and another 6 tests for the perimeter method of each subclass. The minimum is 6 but more is preferable.'''



from unittest import TestCase
from person import Triangle, Circle, Square

class TestTriangle(TestCase):
    def setUp(self):
        print("Starting triangle tests")
        self.triangle = Triangle(3, 4, 3, 4)

    def test_area(self):
        self.assertEqual(self.triangle.area(), 6)
        self.assertEqual(Triangle(5, 10, 5, 5).area(), 25)
        self.assertEqual(Triangle(0, 10, 5, 5).area(), 0)
        self.assertEqual(Triangle(8, 2, 8, 8).area(), 8)
        self.assertEqual(Triangle(6, 3, 6, 6).area(), 9)
        self.assertEqual(Triangle(10, 0, 10, 10).area(), 0)

    def test_perimeter(self):
        self.assertEqual(self.triangle.perimeter(), 10)
        self.assertEqual(Triangle(5, 10, 5, 5).perimeter(), 15)
        self.assertEqual(Triangle(0, 10, 5, 5).perimeter(), 10)
        self.assertEqual(Triangle(8, 2, 8, 8).perimeter(), 24)
        self.assertEqual(Triangle(6, 3, 6, 6).perimeter(), 18)
        self.assertEqual(Triangle(10, 0, 10, 10).perimeter(), 30)

    def test_absolutely_nothing(self):
        self.assertEqual("Rafi", "Rafi")

    def tearDown(self):
        del self.triangle
        print("All tests for triangle has been executed.")

class TestCircle(TestCase):
    def setUp(self):
        self.circle = Circle(5)

    def test_area(self):
        self.assertAlmostEqual(self.circle.area(), 78.53981633974483, places=5)
        self.assertAlmostEqual(Circle(1).area(), 3.141592653589793, places=5)
        self.assertAlmostEqual(Circle(0).area(), 0, places=5)
        self.assertAlmostEqual(Circle(10).area(), 314.1592653589793, places=5)
        self.assertAlmostEqual(Circle(3).area(), 28.274333882308138, places=5)
        self.assertAlmostEqual(Circle(2.5).area(), 19.634954084936208, places=5)

    def test_perimeter(self):
        self.assertAlmostEqual(self.circle.perimeter(), 31.41592653589793, places=5)
        self.assertAlmostEqual(Circle(1).perimeter(), 6.283185307179586, places=5)
        self.assertAlmostEqual(Circle(0).perimeter(), 0, places=5)
        self.assertAlmostEqual(Circle(10).perimeter(), 62.83185307179586, places=5)
        self.assertAlmostEqual(Circle(3).perimeter(), 18.84955592153876, places=5)
        self.assertAlmostEqual(Circle(2.5).perimeter(), 15.707963267949466, places=5)

class TestSquare(TestCase):
    def setUp(self):
        self.square = Square(4)

    def test_area(self):
        self.assertEqual(self.square.area(), 16)
        self.assertEqual(Square(0).area(), 0)
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(10).area(), 100)
        self.assertEqual(Square(1).area(), 1)
        self.assertEqual(Square(2.5).area(), 6.25)

    def test_perimeter(self):
        self.assertEqual(self.square.perimeter(), 16)
        self.assertEqual(Square(0).perimeter(), 0)
        self.assertEqual(Square(5).perimeter(), 20)
        self.assertEqual(Square(10).perimeter(), 40)
        self.assertEqual(Square(1).perimeter(), 4)
        self.assertEqual(Square(2.5).perimeter(), 10)

