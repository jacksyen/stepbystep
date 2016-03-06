def daemonize_app
  if RUBY_VERSION <"2.3"
    exit if fork
    Process.setsid
    puts Process.getsid
    exit if fork
    Dir.chdir "/"
    STDIN.reopen "dev/null"
    STDOUT.reopen "dev/null","a"
    STDERR.reopen "dev/null","a"
  else
    Process.daemon
  end
end