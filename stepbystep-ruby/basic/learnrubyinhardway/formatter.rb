formatter = "%{first} %{second} %{third} %{fourth}"
puts formatter %{first:1,second:2,third:3,fourth:4}
puts formatter %{first:"first",second:"second",third:"third",fourth:"fourth"}
puts formatter %{
               first:"first notes",
               second:"second notes",
               third:"third notes",
               fourth:"fourth notes"
               }


