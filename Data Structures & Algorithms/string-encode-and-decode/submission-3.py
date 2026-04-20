class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size = []
        s = ""
        res = ""
        for ch in strs:
            s+=ch
            size.append(len(ch))
        print(size,s)
        for ch in size:
            res+=str(ch)
            res+=","
        res+="#"
        print(res+s)
        return (res+s)
  
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        parts = s.split('#', 1)
        if len(parts) < 2 or not parts[0]:
            return []

        sizes = [int(x) for x in parts[0].split(',') if x]
        data = parts[1]

        res, idx = [], 0
        for sz in sizes:
            res.append(data[idx:idx + sz])
            idx += sz

        return res









