class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        ret_str = ""
        special = False
        while i < len(path):
            if i > 0 and path[i] == "." and (path[i-1] != "/" and path[i-1] != "."):
                special = True
            if i >= 2 and ((path[i] == "/" and path[i-2:i] == ".." and path[i-3] == "/") or (i == len(path) - 1 and path[i-1:i+1] == ".." and path[i-2] == "/")):
                ln = len(ret_str)
                c = 0
                while c < 2 and ln > 0:
                    if ret_str[ln-1] == "/":
                        c += 1
                    ln -= 1
                ret_str = ret_str[:ln]
                while len(ret_str) > 1 and ret_str[-1] == "/":
                    ret_str = ret_str[:-1]
            elif i >= 1 and path[i-1] == "/" and path[i] == "/":
                i += 1
                continue
            elif i >= 2 and path[i-2] == "/" and path[i-1] == "." and path[i] == "/":
                ln = len(ret_str)
                ret_str = ret_str[:ln-2]
            ret_str += path[i]
            i += 1
        
        if len(ret_str) >= 3 and ret_str[-3:] != "..." and (ret_str[-3] == "/" or ret_str[-2] == "/"):
            while len(ret_str) > 1 and ret_str[-1] == ".":
                ret_str = ret_str[:-1]
        while len(ret_str) > 1 and ret_str[-1] == "/":
            ret_str = ret_str[:-1]

        if special is False and len(ret_str) >= 4 and ret_str[-4:] != "/...":
            while len(ret_str) > 1 and ret_str[-1] == ".":
                ret_str = ret_str[:-1]
        if ret_str == "." or ret_str == "/.":
            ret_str = "/"
        return ret_str