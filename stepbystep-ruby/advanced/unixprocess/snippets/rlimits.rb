Process.getrlimit(:NPROC)

Process.getrlimit(:FSIZE)

Process.getrlimit(:STACK)

Process.setrlimit(:NOFILE,4096)

p Process.getrlimit(:NOFILE)