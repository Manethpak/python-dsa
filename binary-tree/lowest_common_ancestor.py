def lca(root, node1, node2):
    if not root:
        return None

    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root

    # both node is in the left subtree
    if left:
        return left
    # both nodes is in the right subtree
    if right:
        return right

    return None
