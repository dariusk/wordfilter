<?php

  class Wordfilter {
    var $blacklist;
    
    function __construct() {
      $str = file_get_contents(dirname(__FILE__) . "/badwords.json");
      $this->blacklist = json_decode($str, true);
    }
    
    function blacklisted($string) {
      $test_string = strtolower($string);
      foreach ($this->blacklist as $badword) {
        if (strpos($test_string, $badword) !== false) {
          return true;
        }
      }
      
      return false;
    }
    
    function addWords($words) {
      if (!is_array($words)) {
        $words = array($words);
      }
      foreach ($words as $word) {
        array_push($this->blacklist, strtolower($word));
      }
    }
    
    function removeWord($word) {
      $this->blacklist = array_diff($this->blacklist, array(strtolower($word)));
    }
    
    function clearList() {
      $this->blacklist = array();
    }
  }  
  
?>