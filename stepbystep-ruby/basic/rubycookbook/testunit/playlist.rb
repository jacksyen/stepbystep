require_relative 'song.rb'
require 'forwardable'

class Playlist
  extend Forwardable
  def_delegator(:@last,:<<,:add_song)
  def_delegator(:@list,:size,:empty?)

  def initialize
    @list =[]
  end

  def find(title)
    @list.find {|song| song.title==title}
  end
end