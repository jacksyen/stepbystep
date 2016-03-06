require 'gdbm'

GDBM.open("data.dbm",0644,GDBM::WRCREAT | GDBM::SYNC) do |dbm|
  dbm['name']="Simon Patrick"
  dbm['dob'] = "1980-12-06"
  dbm['uses'] = "Ruby"
end

GDBM.open("data.dbm") do |dbm|
  p dbm.keys
  p dbm['dob']
  dbm.delete('dob')
  p dbm.keys
end