require 'minitest/autorun'
require_relative 'playlist.rb'

class TestPlaylist < Test::Unit::TestCase
  def test_adding
    pl = Playlist.new
    assert_empty(pl)
    asset_nil(pl.find("simon patrick"))
    pl.add_song(Song.new("simon patrick","tester"))
    s = pl.find("simon patrick")
    refute_nil(s)
    assert_equal("tester",s.artist)
  end
end