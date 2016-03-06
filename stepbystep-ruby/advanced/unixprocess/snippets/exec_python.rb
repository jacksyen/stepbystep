hosts = File.open('/etc/hosts')
python_code = %Q[import os; print os.fdopen(#{hosts.fileno}).read()]

exec 'python','-c',python_code,{hosts.fileno =>hosts}
