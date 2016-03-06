require 'rexml/document'
include REXML

xml = Document.new(File.open("demo.xml"))

cls = Element.new("class")
cls.attributes["name"] ="Rational"
cls.text ="Represents complext numbers"

int= xml.elements["//class[@name='Integer']"]
int.delete_at(1)
int.delete_at(2)
int.next_sibling =cls

xml.elements.each("//class") do |c|
  c.attributes['class_name']=c.attributes['name']
  c.attributes.delete('name')
end

xml << XMLDecl.new
xml.write(STDOUT,2)