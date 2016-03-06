formatter = "%s %s %s %s"

#formatter as a template
puts formatter % [1, 2, 3, 4]
puts formatter % ["one", "two", "three", "four"]
puts formatter % [true, false, false, true]
#formatter as a String
puts formatter % [formatter, formatter, formatter, formatter]
puts formatter % [
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
]

formatter1="%d %d %d"
puts formatter1 % [23,12,45]
#error wrong arguments for Integer()
puts formatter1 % ["test","456"]