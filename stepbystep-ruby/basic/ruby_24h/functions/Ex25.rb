module Ex25
  def self.break_words(stuff)
    words = stuff.split(' ')
    return words
  end

  def self.sort_words(stuff)
    stuff.sort()
  end

  def self.print_first(words)
    puts words[0]
  end

  def self.print_first_words(words)
    #shift the first word and shifts
    word =words.shift()
    puts word
  end

  def self.print_last_word(words)
    # like a stack
    word =words.pop()
    puts word
    return word
  end

  def self.sort_sentence(sentence)
    words = break_words sentence
    print_first words
    print_last_word words

  end

  def self.print_first_and_last_sorted(sentence)
    words = sort_sentence sentence
    print_first words
    print_last_word words
  end
end

sentence ="this is for testing purpose"

Ex25.sort_sentence sentence