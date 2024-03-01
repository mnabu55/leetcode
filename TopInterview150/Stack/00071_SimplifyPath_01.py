

class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")

        stack = []
        for dir in split_path:
            if dir == "." or dir == "":
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                if dir:
                    stack.append(dir)

        # 以下は自分で作成したコード。24行目で表現できる
        # canonical_path = ""
        # for dir in stack:
        #     canonical_path += "/" + dir

        # return canonical_path if canonical_path != "" else "/"
        return "/" + "/".join(stack)



solution = Solution()
assert solution.simplifyPath("/home/") == "/home"
assert solution.simplifyPath("/../") == "/"

