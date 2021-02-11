Gem::Specification.new do |s|
  s.name        = "wordfilter"
  s.version     = "0.2.6"
  s.date        = "2016-01-30"
  s.summary     = "A small module meant for use in text generators that lets you filter strings for bad words."
  s.description = <<EOF
Wordfilter is a small library that can check a string for blacklisted words.
It comes with a pre-defined list of words, but you can add your own.
EOF
  s.authors     = ["Darius Kazemi", "Eli Brody"]
  s.email       = ["darius.kazemi@gmail.com", "brodyeli@gmail.com"]
  s.files       = ["lib/wordfilter.rb", "lib/badwords.json"]
  s.test_files  = ["test/wordfilter_test.rb"]
  s.homepage    = "https://github.com/dariusk/wordfilter"
  s.license     = "MIT"
end