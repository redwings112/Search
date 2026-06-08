# Define the function that removes a node from the frontier and returns it.
#def remove(self):
    # Terminate the search if the frontier is empty, because this means that there is no solution.
#    if self.empty():
#        raise Exception("empty frontier")
#    else:
        # Save the last item in the list (which is the newest node added)
#        node = self.frontier[-1]
        # Save all the items on the list besides the last node (i.e. removing the last node)
#        self.frontier = self.frontier[:-1]
#        return node

# Define the function that removes a node from the frontier and returns it. 
def remove(self):
    # Terminate the search if the frontier is empty, because this means that there is no solution.
    if self.empty():
        raise Exception("empty frontier")
    else:
        # Save the last item in the list (which is the newest node added)
        node = self.frontier[-1]
        # Save all the items on the list besides the last node (i.e. removing the last node)
        self.frontier = self.frontier[:-1]
        return node
        print(node)
