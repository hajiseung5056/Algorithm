# 이진 검색 트리 클래스 BinarySearchTree 사용하기

from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    s =