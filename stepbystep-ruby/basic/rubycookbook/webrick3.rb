require 'webrick'
include WEBrick

hello_proc = lambda do |req,res|
  res['Content-Type']="text/html"
  res.body = %{
    <html>
      <body><p>test #{req['User-Agent']}  #{req.query.keys.join(", ")}</p></body>
    </html>
  }
end

bye_proc = lambda do |req,res|
  res['Content-Type'] ="text/html"
  res.body = %{
  <html><body><p>good bye</p></body></html>
  }
end

hello = HTTPServlet::ProcHandler.new(hello_proc)
bye = HTTPServlet::ProcHandler.new(bye)

s = HTTPServer.new(:Port =>2000)
s.mount("/hello",hello)
s.mount("/bye",bye)

trap("INT") {s.shutdown}
s.start