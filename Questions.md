1.a

Write a function f :: Char -> Int that converts a character to its score. Lowercase letters score 5 if they are
contained in the word "haskell"; otherwise they score 1. Uppercase letters are worth double: 10 if contained in 
"HASKELL", 2 otherwise. A character that is not a letter scores zero. For example:

    f `A` = 10        f `B` = 2             f`.` = 0
    f `a` = 5         f 'b' = 1		

1.b

Using f, define a list comprehension g :: String -> Int thatgiven  a string will return the sum of the score for each 
letter.

    g "aBc4E" = 100     g "Inf1-FP" = 8          g" Java" = 50


1.c

You guessed it! write a function h, that will do the same thing as g, but as a recursive function instead..



2.
Fizz buzz is a simple game that teachers often use to teach children the 5 and 3 division tables. I've included a 
python implementation which you can check your results against.

3.a
Write a recursive function m :: String->Int that converts a list of base 3 digits to the corresponding numerical base 10 value. For example:

    m "201" = (2*3^2) + (0*3^1) + (1*3^0)
    m "12" = 5
    m "1202 = 47
    m "120221" = 430

3.b
Write a second function n :: String-> Int that has the same functionality as m but is written using a list comprehension.

4.
Write a recursive function o :: [Int] -> Bool that, given a non-empty list of nonzero numbers, returns True if each successive number (except the first) is divisible by its predecessor in the list. The function should give an error if applied to the empty list.
o [1,2,6]  = True
o [3,9,27] = True

4.b
Write a list comprehension p :: [Int] -> Bool that will have the same functionality as o
