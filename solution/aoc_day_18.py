# aoc_day_18.py

from solution.aoc_base import AocBaseClass
from enum import Enum
import io


class NodeType(Enum):
    LEAF = 1
    PAIR = 2


class Node:
    def __init__(self, f):
        self.parent = None
        if isinstance(f, int):
            self.type = NodeType.LEAF
            self.value = f
            return
        elif isinstance(f, tuple):
            self.type = NodeType.PAIR
            self.left = f[0]
            self.right = f[1]
            self.left.parent = self
            self.right.parent = self
            return
        self.parent = None
        c = f.read(1)
        if c == "[":
            self.type = NodeType.PAIR
            self.left = Node(f)
            self.left.parent = self
            assert f.read(1) == ","
            self.right = Node(f)
            self.right.parent = self
            assert f.read(1) == "]"
        else:
            self.type = NodeType.LEAF
            self.value = int(c)
            self.left = None
            self.right = None

    def __str__(self) -> str:
        if self.type == NodeType.PAIR:
            return f"[{self.left},{self.right}]"
        else:
            return f"{self.value}"

    def __repr__(self) -> str:
        return str(self)

    def perform_inorder(self):
        if self.type == NodeType.LEAF:
            yield self
        else:
            for node in self.left.perform_inorder():
                yield node
            yield self
            for node in self.right.perform_inorder():
                yield node

    def depth(self):
        ret = -1
        node = self
        while node is not None:
            node = node.parent
            ret += 1
        return ret

    def magnitude(self):
        if self.type == NodeType.LEAF:
            return self.value
        return self.left.magnitude() * 3 + 2 * self.right.magnitude()


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        puzzle_input = puzzle_input.split("\n")
        return [line.strip() for line in puzzle_input if len(line) > 1]

    DAY = 18

    @staticmethod
    def maybe_explode(root):
        node_list = list(root.perform_inorder())
        for i in range(len(node_list)):
            if node_list[i].depth() >= 4 and node_list[i].type == NodeType.PAIR:
                node_list[i].type = NodeType.LEAF
                node_list[i].value = 0
                for j in range(i - 2, -1, -1):
                    if node_list[j].type == NodeType.LEAF:
                        node_list[j].value += node_list[i].left.value
                        break
                for j in range(i + 2, len(node_list)):
                    if node_list[j].type == NodeType.LEAF:
                        node_list[j].value += node_list[i].right.value
                        break
                return True

    @staticmethod
    def maybe_split(root):
        for node in root.perform_inorder():
            if node.type == NodeType.LEAF and node.value >= 10:
                node.type = NodeType.PAIR
                left = node.value // 2
                node.left = Node(left)
                node.left.parent = node
                node.right = Node(node.value - left)
                node.right.parent = node
                return True
        return False

    @classmethod
    def reduce(cls, root):
        while cls.maybe_explode(root) or cls.maybe_split(root):
            pass
        return root

    @staticmethod
    def parse_line(line):
        f = io.StringIO(line)
        root = Node(f)
        assert f.read() == ""
        return root

    def calculate(self, /, enable_part2=False):
        best = 0
        current = self.reduce(self.parse_line(self.data[0]))
        for index_, i in enumerate(self.data):
            if enable_part2:
                for j in self.data:
                    if i == j:
                        continue
                    line = f"[{i},{j}]"
                    sum_ = self.reduce(self.parse_line(line)).magnitude()
                    if sum_ > best:
                        best = sum_
            else:
                if index_ == 0:
                    continue
                next_ = self.reduce(self.parse_line(self.data[index_]))
                current = self.reduce(Node((current, next_)))
        return current.magnitude(), best

    def part1(self):
        """Solve part 1"""
        return self.calculate()[0]

    def part2(self):
        """Solve part 2"""
        return self.calculate(enable_part2=True)[1]


if __name__ == "__main__":
    AocSolution().print_solution()
