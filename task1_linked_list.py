from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, Tuple


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class LinkedList:
    def __init__(self, values: Iterable[int] = ()):
        self.head: Optional[Node] = None
        for v in reversed(list(values)):
            self.head = Node(v, self.head)

    def to_list(self) -> list[int]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    def reverse(self) -> None:
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def sort(self) -> None:
        self.head = merge_sort(self.head)


def split_middle(head: Optional[Node]) -> Tuple[Optional[Node], Optional[Node]]:
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next.next

    mid = slow.next  # type: ignore[union-attr]
    slow.next = None  # type: ignore[union-attr]
    return head, mid


def merge_sorted(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    dummy = Node(0)
    tail = dummy

    while a and b:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b
    return dummy.next


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return head
    left, right = split_middle(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted(left, right)


def merge_two_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result = LinkedList()
    result.head = merge_sorted(list1.head, list2.head)
    return result


if __name__ == "__main__":
    ll = LinkedList([3, 1, 4, 1, 5, 9, 2])
    print("Original:", ll.to_list())

    ll.reverse()
    print("Reversed:", ll.to_list())

    ll.sort()
    print("Sorted:", ll.to_list())

    a = LinkedList([1, 3, 5, 7])
    b = LinkedList([2, 4, 6, 8])
    merged = merge_two_sorted_lists(a, b)
    print("Merged:", merged.to_list())