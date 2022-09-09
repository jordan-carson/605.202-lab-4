def sortedMerge(left, right):
    pass


def mergesort(head):

    if head is None or head.next is None:
        return head

    sorted = natural_merge_sort(head)
    unsorted = sorted.next

    sorted.next = None
    left = mergesort(head)
    right = mergesort(unsorted)

    return sortedMerge(left, right)


def natural_merge_sort(head):
    if head is None:
        return head

    next = head.next
    curr = head

    while next.val > curr.val:
        next = next.next
        curr = curr.next

    return curr
