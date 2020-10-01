import unittest

# Function fibonacci:
# Parameter: n : ganze Zahl
# Result: Fibonacci-Zahl von n
#
# Jede Zahl ist die Summe ihrer beiden Vorgänger
#
# Iterativ: mit Schleife, anstatt Rekursion


def fibonacci(n):
    if n <= 1:
        return n
    z1 = 0
    z2 = 1
    for _ in range(1, n):
        ergebnis = z1 + z2
        z1 = z2
        z2 = ergebnis

    return ergebnis

# Testcases


class TestBubblesort(unittest.TestCase):
    def test_1(self):
        # Arrange
        n = 1
        expected = 1

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)

    def test_2(self):
        # Arrange
        n = 2
        expected = 1

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)

    def test_3(self):
        # Arrange
        n = 3
        expected = 2

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)

    def test_6(self):
        # Arrange
        n = 6
        expected = 8

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)

    def test_8(self):
        # Arrange
        n = 8
        expected = 21

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)

    def test_30(self):
        # Arrange
        n = 30
        expected = 832040

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)

    def test_41(self):
        # Arrange
        n = 41
        expected = 165580141

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)


# Run Tests
if __name__ == "__main__":
    unittest.main()
