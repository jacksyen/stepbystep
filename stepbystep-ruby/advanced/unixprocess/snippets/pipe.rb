reader,writer = IO.pipe

writer.write("Trying to get the reader to write something")
writer.close
puts reader.read