# typed: strict
# frozen_string_literal: true

require 'sorbet-runtime'
require 'set'

puts "===="

costs = {
    'a' => 1,
}

contents = File.read('lib/day_3.txt')

values = []
items = contents.split("\n")
thruple = T.let([], T::Array[String])
items.each.with_index do |item, idx|
    if idx % 3 == 0 && idx != 0
      set_1 = Set.new
      T.must(thruple[0]).split("").each { set_1.add(_1)}
      set_2 = Set.new
      T.must(thruple[1]).split("").each { set_2.add(_1)}
      set_3 = Set.new
      T.must(thruple[2]).split("").each { set_3.add(_1)}
      values << ((set_1 & set_2 & set_3).first)
      thruple = []
      thruple << item
    else
        thruple << item
    end
end
set_1 = Set.new
T.must(thruple[0]).split("").each { set_1.add(_1)}
set_2 = Set.new
T.must(thruple[1]).split("").each { set_2.add(_1)}
set_3 = Set.new
T.must(thruple[2]).split("").each { set_3.add(_1)}
values << ((set_1 & set_2 & set_3).first)

puts values.map{"'#{_1}'"}.join(", ")

# Then this Java:
# public class MyClass {
#     public static void main(String args[]) {
#       char[] chars = new char[]{'s', 'f', 'N', 'l', 'b', 'v', 'C', 'G', 'N', 'l', 'G', 'V', 'c', 'G', 'q', 'q', 'l', 'l', 'C', 'f', 'l', 'R', 'G', 'N', 'Q', 'V', 'v', 'c', 'S', 'h', 'L', 'g', 'Z', 'w', 'W', 'V', 'H', 'r', 'G', 'n', 't', 'T', 'M', 'b', 'F', 'J', 'q', 'f', 'w', 'Z', 'f', 'g', 'z', 'n', 't', 'z', 'B', 'J', 'P', 'v', 'n', 'C', 'l', 'h', 'c', 'g', 'h', 'd', 's', 'N', 'b', 'M', 'J', 'z', 's', 'T', 'q', 'q', 'b', 'p', 'H', 'V', 'g', 'z', 'Z', 'J', 'q', 'b', 'S', 'j', 's', 'l', 'j', 'Q', 'z', 'M', 'p', 'F', 'R', 'd'};
#       int sum = 0;
#       for (char c : chars) {
#           if (c >= 'a' && c <= 'z') {
#               sum += ((c - 'a') + 1);
#           } else {
#               sum += ((c - 'A') + 27);
#           }
          
#       }
#       System.out.println(sum);
#     }
# }