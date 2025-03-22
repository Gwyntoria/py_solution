from collections import defaultdict, deque


class Solution:

    class DSU:  # Disjoint Set Union
        def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [0] * n

        def find(self, x: int) -> int:
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x: int, y: int) -> bool:
            root_x = self.find(x)
            root_y = self.find(y)

            if root_x == root_y:
                return False

            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

            return True

    def __init__(self):
        pass

    # 5. Longest Palindromic Substring
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        max_len = 0
        start = 0
        str_len = len(s)

        for i in range(str_len):
            # Check for odd-length palindromes centered at i
            left, right = i, i
            while left >= 0 and right < str_len and s[left] == s[right]:
                left -= 1
                right += 1
            current_length = right - left - 1
            if current_length > max_len:
                max_len = current_length
                start = left + 1

            # Check for even-length palindromes centered between i and i+1
            left, right = i, i + 1
            while left >= 0 and right < str_len and s[left] == s[right]:
                left -= 1
                right += 1
            current_length = right - left - 1
            if current_length > max_len:
                max_len = current_length
                start = left + 1

        return s[start : start + max_len]

    # 925. Long Pressed Name
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        name_len = len(name)
        typed_len = len(typed)
        name_index = 0
        typed_index = 0

        while name_index < name_len and typed_index < typed_len:
            if name[name_index] == typed[typed_index]:
                name_index += 1
                typed_index += 1
            else:
                if typed_index == 0:
                    return False
                if typed[typed_index] == typed[typed_index - 1]:
                    typed_index += 1
                else:
                    return False

        if name_index < name_len:
            return False

        if typed_index < typed_len:
            while typed_index < typed_len:
                if typed[typed_index] != name[name_index - 1]:
                    return False
                typed_index += 1
            return True
        else:
            return True

    # 1658. Minimum Operations to Reduce X to Zero
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        total = sum(nums)
        n = len(nums)
        if total < x:
            return -1
        if total == x:
            return n

        target = total - x
        current_sum = 0
        max_len = -1
        left = 0

        for right in range(n):
            current_sum += nums[right]

            # If current_sum exceeds target, move left pointer to reduce the window size
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Check if current window sum equals target and update max length
            if current_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1

    # 733. Flood Fill
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        pre_color = image[sr][sc]
        if pre_color == color:
            return image

        def spread(r, c):
            if image[r][c] == pre_color:
                image[r][c] = color

                if r > 0:
                    spread(r - 1, c)
                if c > 0:
                    spread(r, c - 1)
                if r + 1 < len(image):
                    spread(r + 1, c)
                if c + 1 < len(image[0]):
                    spread(r, c + 1)

        spread(sr, sc)
        return image

    # 3191. Minimum Operations to Make Binary Array Elements Equal to One I
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_len = len(nums)
        ones = sum(nums)

        if ones == 0:
            if array_len % 3 == 0:
                return array_len / 3
            else:
                return -1
        elif ones == array_len:
            return 0

        op = 0

        for i in range(array_len):
            if nums[i] == 0:
                if i + 2 < array_len:
                    for j in range(i, i + 3):
                        if nums[j] == 0:
                            nums[j] = 1
                        else:
                            nums[j] = 0

                    op += 1
                else:
                    for j in range(i, array_len):
                        if nums[j] == 0:
                            return -1

        return op

    # 2685. Count the Number of Complete Components
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: 构建邻接表
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        visited = [False] * n  # 标记节点是否访问过
        result = 0  # 记录完全连通分量的数量

        # Step 2: 遍历所有节点，找到连通分量
        def bfs(start):
            queue = deque([start])
            component = []  # 当前连通分量的节点集合
            while queue:
                node = queue.popleft()
                if not visited[node]:
                    visited[node] = True
                    component.append(node)
                    # 将未访问的邻居加入队列
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            queue.append(neighbor)
            return component

        for i in range(n):
            if not visited[i]:  # 如果当前节点未访问过
                component = bfs(i)  # 找到当前连通分量
                k = len(component)  # 连通分量的节点数
                # Step 3: 判断是否为完全图
                edge_count = sum(len(graph[node]) for node in component) // 2
                if edge_count == k * (k - 1) // 2:
                    result += 1

        return result

    def countCompleteComponents_2(self, n: int, edges: list[list[int]]) -> int:
        dsu = self.DSU(n)
        for a, b in edges:
            dsu.union(a, b)

        adjacency_graphy = defaultdict(set)
        for a, b in edges:
            adjacency_graphy[a].add(b)
            adjacency_graphy[b].add(a)

        dsu_root_set = set()
        for i in range(n):
            root = dsu.find(i)

            if root not in dsu_root_set:
                dsu_root_set.add(root)

        same_dsu_root_dict = defaultdict(set)

        for root in dsu_root_set:
            for i in range(n):
                if dsu.find(i) == root:
                    same_dsu_root_dict[root].add(i)

        result = 0

        for root in dsu_root_set:
            edge_nums = 0
            for a in same_dsu_root_dict[root]:
                edge_nums += len(adjacency_graphy[a])

            edge_nums //= 2
            vertex_nums = len(same_dsu_root_dict[root])
            if edge_nums == vertex_nums * (vertex_nums - 1) // 2:
                result += 1

        return result


if __name__ == "__main__":
    s = Solution()

    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("ac"))
