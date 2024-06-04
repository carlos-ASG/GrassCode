import tkinter as tk
from tkinter import ttk

def draw_tree(canvas, node, x, y, width):
    if node is None:
        return

    text = node.data  # Assuming 'data' is the node's value
    label = ttk.Label(canvas, text=text)
    label.place(x=x, y=y, width=width)

    if node.left:
        draw_tree(canvas, node.left, x - width // 2, y + width, width // 2)
        canvas.create_line(x, y + width // 2, x - width // 2, y + width)

    if node.right:
        draw_tree(canvas, node.right, x + width // 2, y + width, width // 2)
        canvas.create_line(x, y + width // 2, x + width // 2, y + width)

# Assuming you have a BinaryTree class or similar data structure
tree = BinaryTree()
# Populate the tree with data

root = tree.root  # Get the root node

window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

draw_tree(canvas, root, 400, 20, 100)

window.mainloop()

class ASTNode:
    def __init__(self, type, children=None):
        self.type = type
        self.children = children if children else []
