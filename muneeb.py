# Strategy described in Nicky Case's "The Evolution of Trust"
# https://ncase.me/trust/
#
# SIMPLETON: Hi! I try to start by cooperating. If  you cooperate
# back, I do the same thing as my last move, even if it was a mistake.
# If you cheat back, I do the opposite thing as my last move, even
# if it was a mistake.

def strategy(history, memory):
    var=0
    if history.shape[1]<2:
        var=1
    elif history.shape[1]>=2:
        if history[1][-1]==1 & history[1][0]==1:
            var=1
        elif history[1][-1]==1 & history[1][0]==0:
            var=0
        elif history[1][-1]==0 & history[1][0]==0:
            var=0
        elif history[1][-1]==0 & history[1][0]==1:
            var=0
    return var,None  
