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