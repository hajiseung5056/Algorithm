# 커서로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:

    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data
        self.next = next
        self.dnext = dnext


class ArrayLinkedList:
    def __init__(self, capacity: int):
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec

    def delete_index(self, idx: int) -> None:
        if self.deleted == Null:
            delf.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
            cnt = 0
            ptr = self.head
            while ptr != Null:
                if self.n[ptr].data == data:
                    self.current = ptr
                    return cnt
                cnt += 1
                ptr = self.n[ptr].next
            return Null

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >=0

    def add_first(self, data: Any):
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head == Null:
            self.add_first(data)
        else:
            ptr - self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head].next == Null:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[ptr].next = Null
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def