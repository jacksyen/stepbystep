require "../lib/gothoweb/version"
require "sinatra"

module Gothonweb
  get '/' do
    greeting ="hello, world!"
    return greeting
  end
end
