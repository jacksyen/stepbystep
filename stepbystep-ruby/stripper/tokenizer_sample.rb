require 'ripper'

# tokenize
p Ripper.tokenize("x>1?'foo':'bar'")

# Lexing
require 'pp'
pp Ripper.lex("x>1?'foo':'bar'")

# parsing
pp Ripper.sexp("x>1?'foo':'bar'")

# compiling to bytecode
puts RubyVM::InstructionSequence.compile("x > 100 ? 'foo' : 'bar'").disassemble
