child_process = 3
dead_processes = 0

child_process.times do
  fork do
    sleep 3
  end
end

trap(:CHLD) do
  puts Process.wait
  dead_processes +=1
  exit if dead_processes == child_process
end

loop do
  (Math.sqrt(rand(44)**8)).floor
end