require 'rinda/tuplespace'

MY_URI="druby://127.0.0.1:12131"
DRb.start_service(MY_URI,Rinda::TupleSpace.new)
DRb.thread.join
