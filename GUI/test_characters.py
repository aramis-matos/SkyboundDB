from characterClass.Character import Character, compute_advantage

gran = Character('0', "gran")
granMove = gran.df['236236H']
zeta = Character('0', "zeta")
zetaMove = zeta.df["236L/5L"]

compute_advantage(zeta, zetaMove, gran, granMove)
