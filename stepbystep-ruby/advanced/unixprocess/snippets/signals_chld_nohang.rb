child_processes = 3
dead_processes = 0

child_processes.items do
  fork do
    sleep 3
  end
end

$stdout.sync = true

trap(:CHLD) do
  begin
    while pid = Process.wait(-1,Process.WHOHANG)
      puts pid
      dead_processes +=1
    end
  rescue Errorno::ECHILD
  end
end

loop do
  exit if dead_processes == child_processes
  sleep 1
end