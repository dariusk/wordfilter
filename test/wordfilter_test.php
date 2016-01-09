<?php
  // there's probably a test suite for php, but for this quick test just run php wordfilter_test.php
  require_once('../lib/wordfilter.php');
  
  class wordfilter_test {
    var $wordfilter;
    
    function setup() {
      $this->wordfilter = new Wordfilter();
    }

    function teardown() {
      $this->wordfilter = null;
    }

    function test_loading() {
      assert(is_array($this->wordfilter->blacklist));
    }  

    function test_badWords() {
      assert($this->wordfilter->blacklisted(
        'this string contains the word skank'));
      assert($this->wordfilter->blacklisted(
        'this string contains the word SkAnK'));
      assert($this->wordfilter->blacklisted(
        'this string contains the wordskank'));
      assert($this->wordfilter->blacklisted(
        'this string contains the skankword'));
      assert(! $this->wordfilter->blacklisted('this string is clean!'));
    }

    function test_addWords() {
      $this->wordfilter->addWords(array('clean'));
      assert($this->wordfilter->blacklisted(
        'this->string contains the word skank'));
      assert($this->wordfilter->blacklisted('this string is clean!'));
    }

    function test_removeWord() {
      # Act
      $this->wordfilter->removeWord('crip');

      # Assert
      assert(! $this->wordfilter->blacklisted('I have a prescription.'));
    }

    function test_remove_multiple_added_words() {
      # Arrange
      # Add several to make sure all instances are removed:
      $this->wordfilter->addWords(array('crip', 'crip'));

      # Act
      $this->wordfilter->removeWord('crip');

      # Assert
      assert(! $this->wordfilter->blacklisted('I have a prescription.'));
    }

    function test_remove_unblacklisted_word() {
      # Arrange
      # Make sure no error when removing a word that's not on the list
      assert(! $this->wordfilter->blacklisted('this string is clean!'));

      # Act
      $this->wordfilter->removeWord('clean');

      # Assert
      assert(! $this->wordfilter->blacklisted('this string is clean!'));
    }

    function test_clearList() {
      $this->wordfilter->clearList();
      assert(! $this->wordfilter->blacklisted(
        'this string contains the word skank'));

      $this->wordfilter->addWords(array('skank'));
      assert($this->wordfilter->blacklisted(
        'this string contains the word skank'));
    }

    function test_add_multiple_words() {
        # Arrange
        $this->wordfilter->clearList();

        # Act
        $this->wordfilter->addWords(array('zebra', 'elephant'));

        # Assert
        assert($this->wordfilter->blacklisted('this->string has zebra in it'));
        assert($this->wordfilter->blacklisted('this->string has elephant in it'));
        assert(! $this->wordfilter->blacklisted('this->string has nothing in it'));
    }
  }
  
  $a = $test->test_loading;
  
  $funcs = explode(" ", "test_loading test_badWords test_addWords test_removeWord test_remove_multiple_added_words test_remove_unblacklisted_word test_clearList test_add_multiple_words");
  foreach ($funcs as $func) {
    $test = new wordfilter_test();
    $test->setup();
    $test->$func();
  }
   
?>