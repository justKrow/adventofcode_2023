# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

file = open("day1/input.txt", "r")
sum = 0;
for words in file:
  for letter in words:
    if letter.isdigit():
      firstDigit = letter
      break
  for letter in words:
    if letter.isdigit():
      lastDigit = letter
  number = firstDigit + lastDigit
  sum = int(number) + sum

print(sum)