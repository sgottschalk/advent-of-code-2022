# typed: strict
# frozen_string_literal: true

require 'sorbet-runtime'

contents = File.read('lib/day_1_1.txt')

per_elf = contents.split("\n\n")
total_per_elf = per_elf.map do |elf_food|
  elf_food.split.map(&:to_i).sum
end
puts T.must(total_per_elf.sort.reverse[0..2]).sum
