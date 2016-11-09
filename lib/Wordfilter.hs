-- |
-- Module: Wordfilter
-- License: MIT
-- Portability: portable
--
-- Haskell port of Darius Kazemi's Wordfilter

module Wordfilter
    (
     -- Immutability changes some of the functionality:
     -- addWords and removeWord return changed copies of
     -- the list instead of changing the list itself. To
     -- address this, we export "raw" and "convenience"
     -- versions of those functions. The "raw" versions
     -- (marked with a ') take an IO [String] wordlist,
     -- while the "convenience" versions "bake in" the
     -- original blacklist. Similarly, clearList is
     -- just an empty list, which can be passed to
     -- the "raw" functions to build up a fresh list.
     -- Examples:
     --
     -- blacklisted "foo" // IO False
     -- clearList >>= addWords ["foo", "bar"] >>= blacklisted' "foo" // IO True
     -- 
     -- real blacklist
       blacklist
     -- empty "blacklist"
     , clearList
     -- "convenience" functions
     , blacklisted
     , addWords
     , removeWord
     -- "raw" functions
     , blacklisted'
     , addWords'
     , removeWord'
     ) where


import Data.Aeson
import Data.Bits ((.|.))
import qualified Data.ByteString.Lazy as B
import Data.Maybe (maybeToList)
import Data.List (intersperse)
import Text.Regex.PCRE

import Paths_wordfilter (getDataFileName)

blacklist :: IO [String]
blacklist = getDataFileName "badwords.json" >>=
            B.readFile >>=
            (return . concat . maybeToList . decode)

clearList :: IO [String]
clearList = return []

blacklisted' :: String -> [String] -> IO Bool
blacklisted' _ [] = return False
blacklisted' s bl = return $ matchTest re s where
    re = makeRegexOpts (defaultCompOpt .|. compCaseless)
                       defaultExecOpt
                       (concat $ intersperse "|" bl)

blacklisted :: String -> IO Bool
blacklisted s = blacklist >>= (blacklisted' s)

addWords' :: [String] -> [String] -> IO [String]
addWords' ws bl = return $ bl ++ ws

addWords :: [String] -> IO [String]
addWords ws = blacklist >>= addWords' ws

removeWord' :: String -> [String] -> IO [String]
removeWord' w bl = return $ filter (not . (== w)) bl

removeWord :: String -> IO [String]
removeWord w = blacklist >>= (removeWord' w)

