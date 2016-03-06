encoding = Encoding.list.each_with_object({}) do |enc,full_list|
  full_list[enc.name]=[enc.name]
end

Encoding.aliases.each do |alias_name,base_name|
  fail "#{base_name} #{alias_name}" unless encoding[base_name]
  encoding[base_name]<<alias_name
end
puts encoding

puts(encoding.values.sort_by { |base_name,*| base_name.downcase}
    .map do |base_name,*rest|
      puts rest
      if rest.empty?
        base_name
      else
        "#{base_name} (#{rest.join(', ')})"
      end
  end)