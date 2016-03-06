2.times do
  fork do
    abort "Finished"
  end
end

puts Process.wait
sleep 5

puts Process.wait