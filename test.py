import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, Node)):
            return False
        return self.freq == other.freq

def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heap.append(Node(char, freq))
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    return heap[0]

def huffman_encoding(data):
    freq_dict = Counter(data)
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_code = {}
    def dfs(node, code):
        if node.char:
            huffman_code[node.char] = code
            return
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")
    dfs(huffman_tree, "")
    encoded_data = "".join([huffman_code[char] for char in data])
    return encoded_data, huffman_code

def main():
    with open('textes/texte_5.txt', 'r') as file:
        data = file.read()
        encoded_data, huffman_code = huffman_encoding(data)
        print("Original data:", data)
        print("Encoded data:", encoded_data)
        print("Huffman code:", huffman_code)

if __name__ == "__main__":
    main()
