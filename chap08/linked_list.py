# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:

    def __init__(self, data: Any= None,next: Node = None):
        self.data = data
        self.next = data


class LinkedList:

    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:

        return self.no

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:

        return self.search(data) >= 0