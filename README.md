# unit-test-pair-python

[bowling-game-kata](https://kata-log.rocks/bowling-game-kata)

[zombie](https://blog.wingman-sw.com/tdd-guided-by-zombies)

Start testing run ```pytest```

Start running main ```python main.py```

## Tests

### assertEqual(a, b)
a == b

### assertNotEqual(a, b)
a != b

### assertTrue(x)
bool(x) is True

### assertFalse(x)
bool(x) is False

### assertIs(a, b)
a is b

### assertIsNot(a, b)
a is not b

### assertIsNone(x)
x is None

### assertIsNotNone(x)
x is not None

### assertIn(a, b)
a in b

### assertNotIn(a, b)
a not in b

### assertIsInstance(a, b)
isinstance(a, b)

### assertNotIsInstance(a, b)
not isinstance(a, b)

### assertRaises(exc, fun, args, *kwds)
fun(*args, **kwds) raises exc

### assertAlmostEqual(a, b)
round(a-b, 7) == 0

### assertNotAlmostEqual(a, b)
round(a-b, 7) != 0

### assertGreater(a, b)
a > b

### assertGreaterEqual(a, b)
a >= b

### assertLess(a, b)
a < b

### assertLessEqual(a, b)
a <= b

### assertRegexpMatches(s, r)
r.search(s)

### assertNotRegexpMatches(a, b)
not r.search(s)

### assertItemsEqual(a, b)
sorted(a) == sorted(b)
Works with unhashable objects

### assertDictContainsSubset(a, b)
All the key/value pairs in a exist in b
