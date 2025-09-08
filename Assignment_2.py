#!/usr/bin/env python3

# Name: Iqbal Jassal
# Date: 09/08/2025
# Assignment 2: Bayes Filter Simulation

# import required libraries
import numpy.random as random
import matplotlib.pyplot as plt

# measurement - based on current state of robot
def get_measurement( current_state_condition = None ):
    if current_state_condition is None:
        return
    
    # simulate measurement
    random_value = random.rand()

    # if currently robot is facing a wall
    if current_state_condition == 'wall':
        if ( random_value <= 0.25 ):
            measurement = 'door'
        else:
            measurement = 'wall'
            
    # if current state is in front of door 
    if current_state_condition == 'door':
        if ( random_value <= 0.3 ):
            measurement = 'wall'
        else:
            measurement = 'door'

    return measurement

# method to calculate measurement probabilities 
def get_measurement_probability( state = None, measurement = None ):
    if ( state == 'P0' or state == 'P2' ):
        if ( measurement == 'wall' ):
            return 0.75
        elif ( measurement == 'door' ):
            return .25
    
    if ( state == 'P1' or state == 'P3' ):
        if ( measurement == 'wall' ):
            return .3
        elif ( measurement == 'door' ):
            return .7
        
    return 0

# method to calculate belief_bar - Predicition step 
def compute_belief( belief ):

    number_of_states = len( belief )
    belief_bar = [0.0] * number_of_states

    # movement probabilities
    stay = 0.2
    move_1_grid = 0.7
    move_2_grids = 0.1

    for x_t in range( number_of_states ):
        for x_o in range( number_of_states ):
            prob = 0.0
            if x_t == x_o:
                prob = stay
            elif x_t == x_o + 1:
                prob = move_1_grid
            elif x_t == x_o + 2:
                prob = move_2_grids
            else:
                prob = 0.0

            belief_bar[ x_t ] += prob * belief[ x_o ]

    return belief_bar

# update step - apply measurement and normalize
def update( belief_bar, measurement ):
    
    number_of_states = len(belief_bar)
    updated_belief = []
    states = [ 'P0', 'P1', 'P2', 'P3' ]

    for i in range( number_of_states ):
        state = states[ i ]
        measurement_prob = get_measurement_probability( state, measurement )
        updated_belief.append( belief_bar[ i ] * measurement_prob )

    # normalization - simplify this step
    total = sum( updated_belief )
    if total != 0:
        updated_belief = [ b / total for b in updated_belief ]

    return updated_belief


def main():
    print( 'Assignment 2 - Bayes Filter' )
    print( '----------------------------\n' )

    # constants
    number_of_iterations = 5
    number_of_states = 4

    # states of robot
    states = [ 'P0', 'P1', 'P2', 'P3' ]

    # initial belief: starting from P0
    belief = [ 1.0, 0.0, 0.0, 0.0 ]

    # all the beliefs 
    beliefs = []

    for iteration in range( number_of_iterations ):
        print( 'Stage:', iteration + 1 )
        print( 'Current belief:', [ round( b, 2 ) for b in belief ] )

        # calculate belief bar
        belief_bar = compute_belief( belief )
        print( 'Belief_bar (prediction):', [ round(b, 2) for b in belief_bar ] )

        # most likely predicted state
        max_index = belief_bar.index( max( belief_bar ) )
        current_state = states[ max_index ]

        # get measurement - rocot facing wall or door
        if ( current_state == 'P0' or current_state == 'P2' ):
            facing = 'wall'
        else:
            facing = 'door'
        
        measurement = get_measurement( facing )
        print( 'Measurement (robot facing):', measurement )

        # update belief based on measurement
        belief = update( belief_bar, measurement )

        print( 'Updated belief:' ) 
        for index, state in enumerate( states ):
            print( f'{ index } { state }: { round( belief[ index ], 2 ) }' )
        print( '-------------------------------------------------\n' )


        beliefs.append( belief.copy() )

    # plotting - beliefs for each iteration (stage)
    for i in range( len( beliefs ) ):
        plt.bar( states, beliefs[ i ])
        plt.title( f"Belief after Step {i + 1}" )
        plt.ylim( 0, 1 )
        plt.ylabel( "Probability" )
        plt.show()


if __name__ == "__main__":
    main()