from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_map = {}  # baseName : largest k suffix
        res = []

        for base in names:
                if base in name_map:
                # find k
                k = name_map[base] + 1
                while f'{base}({k})' in name_map:
                    k += 1
                name_map[base] = k
                base = f'{base}({k})'  # base with suffix is considered a base name

            name_map[base] = 0  # first time seeing this base name
            res.append(base)
        return res


ins = Solution()
assert ins.getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]) == ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"], "case 1 ng"
