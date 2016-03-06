require 'socket'

Socket.pair(:UNIX,:DGRAM,0)
