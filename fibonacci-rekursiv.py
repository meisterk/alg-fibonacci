import unittest

# Function fibonacci:
# Parameter: n : ganze Zahl
# Result: Fibonacci-Zahl von n
#
# Jede Zahl ist die Summe ihrer beiden Vorgänger


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

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
        expected = 102334155

        # Act
        result = fibonacci(n)

        # Assert
        self.assertEqual(result, expected)


# Run Tests
if __name__ == "__main__":
    unittest.main()
