def get_action_value(mdp, state_values, state, action, gamma):
    """ Computes Q(s,a) as in formula above """
    s = 0
    for next_state, next_state_value in state_values.items():
        env_dynamic = mdp.get_transition_prob(state=state, action=action, next_state=next_state)
        s += env_dynamic * (mdp.get_reward(state=state, action=action, next_state=next_state) + gamma * next_state_value)
    return s
