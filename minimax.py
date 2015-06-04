"""
idocstring
"""
def evaluate(game_state):
    return 0

def min_play(game_state):
    if game_state.is_gameover():
        return evaluate(game_state)
    moves = game_state.get_available_moves()
    best_score = float('inf')
    for move in moves:
        clone = game_state.next_state(move)
        score = max_play(clone)
        if score < best_score:
            best_move = move
            best_score = score
    return best_score


def max_play(game_state):
    if game_state.is_gameover():
        return evaluate(game_state)
    moves = game_state.get_available_moves()
    best_score = float('-inf')
    for move in moves:
        clone = game_state.next_state(move)
        score = min_play(clone)
        if score > best_score:
            best_move = move
            best_score = score
    return best_score


def minimax(game_state):
    moves = game_state.get_available_moves()
    best_move = moves[0]
    best_score = float('-inf')
    for move in moves:
        clone = game_state.next_state(move)
        score = min_play(clone)
        if score > best_score:
            best_move = move
            best_score = score
    return best_move

