from Character import Character, compute_advantage

gram = Character(0, "gran")
gram2 = Character(0, "gran")
gram_move = gram.df['214L']
gram2_move = gram2.df['ACXX']

compute_advantage(gram, gram_move, gram2, gram2_move)



#gram.print_fd()