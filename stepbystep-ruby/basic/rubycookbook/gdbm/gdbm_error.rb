require 'gdbm'

GDBM.open("data.dbm",0,GDBM::READER) do |dbm|
  p dbm.keys
  dbm.delete('name')
end