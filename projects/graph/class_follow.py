# traversal pseudocode
# Create a queue/stack as appropriate
# Put the starting point in that
# Make a set to keep track of where we’ve been
# While there is stuff in the queue/stack
#    Pop the first item
#    If not visited
#       DO THE THING!
#       Add to visited
#       For each edge in the item
#           Add that edge to the queue/stack
