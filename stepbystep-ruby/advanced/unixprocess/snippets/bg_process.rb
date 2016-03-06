message = 'Good Morning'
recipient = 'simonpatrick@163.com'

fork do
  StatsCollector.record message,recipient
end