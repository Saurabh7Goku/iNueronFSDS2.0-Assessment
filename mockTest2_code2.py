class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addingList(l1, l2):
    dummy = ListNode()  # Dummy node to track the head of the sum linked list
    curr = dummy  # Current node to track the current position in the sum linked list
    carry = 0  # Carry to store the carry value from one digit to the next

    while l1 or l2 or carry:
        # Get the values of the current digits
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # Calculate the sum of the current digits and the carry
        total = x + y + carry

        # Determine the value of the current digit and the new carry
        digit = total % 10
        carry = total // 10

        # Create a new node with the current digit and add it to the sum linked list
        curr.next = ListNode(digit)
        curr = curr.next

        # Move to the next nodes of both linked lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next  # Return the head of the sum linked list


# Utility function to convert a list to a linked list
def listToLinkedList(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Utility function to convert a linked list to a list
def linkedListToList(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# TryOut 1
l1 = listToLinkedList([2, 4, 3])
l2 = listToLinkedList([5, 6, 4])
result = addingList(l1, l2)
print(linkedListToList(result))
# Output: [7, 0, 8]
