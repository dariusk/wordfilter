require 'json'

module Wordfilter
	BadWordsFileName = File.dirname(__FILE__) + "/badwords.json";
	ScatologicalWordsFileName = File.dirname(__FILE__) + "/scatological_words.json";
	@@blacklist = nil

	def self.init_first_time
		return if(!@@blacklist.nil?)
		self.init
	end

	def self.init
		badwords_file = File.read(BadWordsFileName);
		@@blacklist = JSON.parse(badwords_file);
	end

	def self.blacklisted? string
		self.init_first_time

		string_to_test = string.downcase
		@@blacklist.map!{|badword| badword.downcase}

		@@blacklist.each{|word|
			return true if string_to_test.include? word
		}

		return false
	end

	def self.add_words words
		self.init_first_time
		@@blacklist += words
	end

	def self.add_scatological_words
		scatological_words_file = File.read(ScatologicalWordsFileName);
		@@scatological_words = JSON.parse(scatological_words_file);
		self.add_words(@@scatological_words)
	end

	def self.clear_list
		@@blacklist = []
	end
end
