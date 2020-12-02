module Day1 where

import System.Environment
import System.IO
import Data.List.Split
import Data.Set (member, fromList)
import Text.Printf

run :: IO ()
run = do
    input <- map read.lines <$> readFile "data/Day1.txt"
    printf "Part 1:\t%d\n" $ p1 input
    printf "Part 2:\t%d\n" $ p2 input

p1 :: [Int] -> Int
p1 input = head [x * (2020 - x) | x <- input, member (2020 - x) set]
    where
        set = fromList input

p2 :: [Int] -> Int
p2 input = head [ x * y * (2020 - (x+y)) | x <- input, y <- input, member (2020 - (x+y)) set]
    where 
        set = fromList input
