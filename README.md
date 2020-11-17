# Raindrops

A function that takes an input number n and return an appended string according to matched numbers of factors.

Conditions
- Factor of 3, print 'Pling'
- Factor of 5, print 'Plang'
- Factor of 7, print 'Plong'
- Else, print original number as string

## Example
- 28 is factor of 1,2,4,7,14,28, print 'Plong'
- 30 is factor of 1,2,3,5,6,10,15,30, print 'PlingPlang'
- 34 is factor of 1,2,17,34, print '34'

## Dev
### Unit testing
```bash
python -m unittest test_raindrop
```
(No need for this too complex)
https://docs.python.org/3.3/library/argparse.html

Mocking input in python
```
https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
```

Mocking exception raise
```
https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects
```