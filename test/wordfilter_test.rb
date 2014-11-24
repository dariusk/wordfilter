$:.unshift(File.dirname(__FILE__) + '/../lib/')

require 'test/unit'
require 'wordfilter'

class WordfilterTest < Test::Unit::TestCase

	def setup
		super
		Wordfilter.init
	end

	def test_detects_bad_words_in_a_string 
		assert(Wordfilter::blacklisted?("this string contains the word skank"), "Failed to mark a bad string as bad.");
		assert(Wordfilter::blacklisted?("this string contains the word SkAnK"), "Failed to mark a bad string as bad.");
		refute(Wordfilter::blacklisted?("this string was clean!"), "Failed to allow a non-bad string.");
	end
	
	def test_add_word_to_blacklist
		Wordfilter::add_words(['clean']);
		assert(Wordfilter::blacklisted?("this string was clean!"), "Failed to blacklist a string containing a new bad word.");
	end
	
	def test_added_words_checked_case_insensitively
		Wordfilter::add_words(['CLEAN']);
		assert(Wordfilter::blacklisted?("this string was clean!"), "Failed to blacklist a string containing a new bad word because of casing differences.");
	end
	
	def test_clear_blacklist
		Wordfilter::clear_list
		refute(Wordfilter::blacklisted?("this string contains the word skank"), "Cleared word list still blacklisting strings.");
		Wordfilter::add_words(['skank']);
		assert(Wordfilter::blacklisted?("this string contains the word skank"), "Failed to blacklist a string containing a new bad word.");
	end
end