module Wordlist_Test where

import Wordlist (blacklisted', addWords', removeWord')
import Test.HUnit

blacklistedTests = TestList [testEmptyFalse, testContained, testNotContained]
testEmptyFalse = TestCase (do r <- blacklisted' "foo" []
                              assertEqual "always false on empty list" False r)
testContained = TestCase (do r <- blacklisted' "i am foo" ["bar", "foo"]
                             assertEqual "should match" True r)
testNotContained = TestCase (do r <- blacklisted' "quux i am" ["bar", "foo"]
                                assertEqual "should not match" False r)


addWordsTest = TestList [testAdd]
testAdd = TestCase (do r <- addWords' ["foo"], ["bar", "baz"]
                       assertEqual "add words to list" ["bar", "baz", "foo"] r)

removeWordTests = TestList [testPresent, testAbsent]
testPresent = TestCase (do r <- removeWord' "foo" ["foo", "bar"]
                           assertEqual "remove word from list" ["bar"] r)
testAbsent = TestCase (do r <- removeWord' "foo" ["bar", "baz"]
                          assertEqual "don't remove absent word" ["bar", "baz"] r)

main = runTestTT $ TestList [blackListedTests, addWordsTest, removeWordsTest]
