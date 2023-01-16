class Solution:
    def sortedListToBST(self, head):
        def BSTCreation(start,end):
            if start==end:
                return None
            slow = start
            fast = start.next
            while fast and fast.next and fast!=end and fast.next!=end:
                slow = slow.next
                fast = fast.next.next
            return TreeNode(slow.val,BSTCreation(start,slow),BSTCreation(slow.next,end))
        return BSTCreation(head,None)
