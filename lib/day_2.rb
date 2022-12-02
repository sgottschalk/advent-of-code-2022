# typed: strict
# frozen_string_literal: true

require 'sorbet-runtime'

contents = File.read('lib/day_2.txt')

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# part 2:  X means you need to lose, Y means you need to end the round in a draw, and Z
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
score_guide = {
  'X': {
    'A': 3,
    'B': 0,
    'C': 6
  },
  'Y': {
    'A': 6,
    'B': 3,
    'C': 0
  },
  'Z': {
    'A': 0,
    'B': 6,
    'C': 3
  }
}
move_score = {
  'X': 1, 'Y': 2, 'Z': 3
}

my_move_per_outcome = {
  'X': {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
  },
  'Y': {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
  },
  'Z': {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
  }
}

rounds = contents.split("\n")
score_per_round = rounds.map do |round|
  them, outcome = round.split(' ')
  them = T.must(them).to_sym
  me = my_move_per_outcome[T.must(outcome).to_sym][them].to_sym
  move_score[me] + score_guide[me][them]
end
puts score_per_round.sum
