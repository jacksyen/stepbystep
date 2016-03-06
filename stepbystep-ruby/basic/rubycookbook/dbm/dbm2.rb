require 'dbm'

DBM.open("/etc/aliases",nil) do |dbm|
  p dbm.keys
  p dbm["postfix\000"]
end