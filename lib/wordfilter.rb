require 'json'

module Wordfilter
	BadWordsFileName = File.dirname(__FILE__) + "/badwords.json"
	@@blacklist = nil
	
	def self.init_first_time
		return if(!@@blacklist.nil?)
		self.init
	end
	
	def self.init
		badwords_file = File.read(BadWordsFileName)
		@@blacklist = JSON.parse(badwords_file)
		@@blacklist.map!(&:downcase)
		return
	end
	
	def self.blacklisted? string
		self.init_first_time
		
		string_to_test = string.downcase
		
		@@blacklist.each{|word|
			return true if string_to_test.include? word
		}
		
		return false
	end
	
	def self.add_words words
		self.init_first_time
		words.map!(&:downcase)
		@@blacklist += words
		return
	end

	def self.remove_word word
		self.init_first_time
		@@blacklist.delete word.downcase
		return
	end
	
	def self.clear_list
		@@blacklist = []
		return
	end
end