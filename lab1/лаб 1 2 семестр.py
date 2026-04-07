import unittest

def find_kth_largest(numbers, k):
    if len(numbers) < k:
        raise ValueError("Розмір масиву повинен бути не менше k")

    sorted_numbers = sorted(numbers, reverse=True)
    kth_largest = sorted_numbers[k - 1]
    index = numbers.index(kth_largest)

    return kth_largest, index


class TestFindKthLargest(unittest.TestCase):
    def test_example(self):
        numbers = [15, 7, 22, 9, 36, 2, 42, 18]
        k = 3
        self.assertEqual(find_kth_largest(numbers, k), (22, 2))

    def test_first_largest(self):
        numbers = [1, 5, 3]
        k = 1
        self.assertEqual(find_kth_largest(numbers, k), (5, 1))

    def test_invalid_k(self):
        numbers = [10, 20]
        k = 5
        with self.assertRaises(ValueError):
            find_kth_largest(numbers, k)


if __name__ == "__main__":
    nums = [15, 7, 22, 9, 36, 2, 42, 18]
    k_val = 3

    try:
        element, position = find_kth_largest(nums, k_val)
        print(f"Вхідний масив: {nums}")
        print(f"Знайдений {k_val}-й найбільший елемент: {element}")
        print(f"Позиція елемента в масиві: {position}")
    except ValueError as e:
        print(e)

    print("\n--- Running Tests ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)