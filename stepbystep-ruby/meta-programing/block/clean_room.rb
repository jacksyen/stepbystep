class CleanRoom
  def current_temperature
    11
  end
end

clean_room = CleanRoom.new
clean_room.instance_eval do
  if current_temperature < 20
    p 'cold'
  end
end

result = clean_room.instance_eval {current_temperature}

p result