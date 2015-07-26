import unittest

# create a new subclass of unittest.TestCase called ExampleTests
class ExampleTests(unittest.TestCase):
	# a test for the implementation of a fizzbuzz function
    def fizzbuzz_goodtest(f):
    output = []
    for n in range(100):
        output.append(str(f(n) + "\n"))
	# where fizzbuzz-output.txt contains 100 lines of expected output
    expected = open("fizzbuzz-output.txt", "r")
    i = 0
    for line in expected:
        if line == output[i]:
            print("Success!")
            i += 1
        else:
            print("Nope. Try Again.")

if __name__ == "__main__":
    unittest.main()

