# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# STEP 0 - TODO
## defining our data structures
class Node: # NOT given to students
    weight : int
    letters : str
    left: any
    right: any
    
    def __init__(self, letters = None, weight = None, left = None, right = None):
        self.weight = weight
        self.letters = letters
        self.left = left
        self.right = right

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letters != None: # if 'TODO': # TODO
        coding[v.letters] = path # TODO
    else:
        retrieve_codes(v.left, path + '0') # TODO
        retrieve_codes(v.right, path + '1') # TODO

# STEP 1
## counting the frequencies - TODO
for i in message:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


# STEP 2
## initialize the nodes - TODO
for letters, count in freq.items():
    nodes.append(Node(letters, count))

# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    combined = Node(None, min_a.weight + min_b.weight, min_a, min_b) # TODO

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
for i in message:
    result += str(coding[i]) # TODO (hint coding[letter] -> code)

# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')