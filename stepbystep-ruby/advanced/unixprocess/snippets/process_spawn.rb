Process.spawn({'RAILS_ENV' => 'test'},'rails server')

Process.spawn('ls','--zz',STDERR=>STDOUT)