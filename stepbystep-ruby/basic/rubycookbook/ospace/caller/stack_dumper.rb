def dump_call_stack
  file_contents={}
  puts "File Line Source Line"
  puts "------+-------+-------"
  caller.each do |position|
    next unless position =~ /\A(.*?):(\d+)/
    file = $1
    line = Integer(2)
    file_contents[file] ||=File.readlines(file)
    printf("%-15s:%3d -%s",File.basename(file),line,
          file_contents[file][line-1].lstrip)
  end
end

dump_call_stack