class Module

  def rake_extension(method)
    if(method_defined?(method))
      $stderr.puts "WARNING:Possible confict"
        "#{self}##{method} already exists"
    else
      yield
    end
  end
end