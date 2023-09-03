from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = path.split("/")
        canonical: List[str] = []
        for dir in directory:
            if not dir or dir == ".":
                continue
            if dir == "..":
                if len(canonical) > 0:
                    canonical.pop()
                continue
            canonical.append(dir)
        return "/" + "/".join(canonical)


print(Solution().simplifyPath("/home/"))
