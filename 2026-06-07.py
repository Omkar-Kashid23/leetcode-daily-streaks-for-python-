class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_dict = {}
        child_set = set()

        # Unpacking the list directly makes the code cleaner
        for parent_val, child_val, is_left in descriptions:
            
            # 1. Create or fetch the parent node
            if parent_val in node_dict:
                parent_node = node_dict[parent_val]
            else:
                parent_node = TreeNode(parent_val)
                node_dict[parent_val] = parent_node
                
            # 2. Create or fetch the child node
            if child_val in node_dict:
                child_node = node_dict[child_val]
            else:
                child_node = TreeNode(child_val)
                node_dict[child_val] = child_node
                
            # 3. Connect them
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
                
            # 4. Add the child's integer value to the set
            child_set.add(child_val)

        # 5. Find the root (the only node value not in the child_set)
        for val, node in node_dict.items():
            if val not in child_set:
                return node
