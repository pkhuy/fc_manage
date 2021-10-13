# A Huffman Tree Node
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''


codes = dict()


def calculate_codes(node, val=''):
    new_value = val + str(node.code)

    if(node.left):
        calculate_codes(node.left, new_value)
    if(node.right):
        calculate_codes(node.right, new_value)

    if(not node.left and not node.right):
        codes[node.symbol] = new_value

    return codes


def calculate_probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


def output_encode(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


def huffman_encoding(data):
    symbol_with_probs = calculate_probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # sap xep
        nodes = sorted(nodes, key=lambda x: x.prob)
        # chon 2 node nho nhat
        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        newNode = Node(left.prob+right.prob, left.symbol +
                       right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calculate_codes(nodes[0])
    print("symbols with codes", huffman_encoding)
    encoded_output = output_encode(data, huffman_encoding)
    return encoded_output, nodes[0]


def huffman_decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string


if __name__ == '__main__':
    alphabet = {
        'a': 0.5,
        'b': 0.3,
        'c': 0.2
    }

    source_data = 'aaabbc'

    #huffman
    if sum(alphabet.values()) != 1:
        raise "Total probability is not equal 1."
    else:
        alphabet_sorted = {k: v for k, v in sorted(
            alphabet.items(), key=lambda item: item[1],  reverse=True)}
        probability = alphabet.values()
        probability = sorted(probability, reverse=True)
        var_to_floor = 10

        data = []
        #thay doi xac suat cua symbol thanh so lan xuat hien
        while(var_to_floor*probability[len(probability)-1] - int(var_to_floor*probability[len(probability)-1]) != 0):
            var_to_floor *= 10
        for key in alphabet.keys():
            data.append(key * int(alphabet[key] * var_to_floor))

        data = "".join(data)

        encoding, tree = huffman_encoding(data)
        print("Encoded output", encoding)
        print("Decoded Output", huffman_decoding(encoding, tree))

    #shannon_fano
