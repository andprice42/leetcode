class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = ""
        wrd_cnt = 0
        for word in words:
            if len(line) == 0:
                wrd_cnt += 1
                line += word
            elif len(line) + len(word) < maxWidth:
                line += (" " + word)
                wrd_cnt += 1
            else:
                num_spaces = maxWidth - len(line) - wrd_cnt + 1
                nline_arr = line.split()
                v = wrd_cnt - 1
                if v > 0:
                    num_per_space = num_spaces // v
                while v > 0:
                    nline_arr[v-1] += " "
                    for i in range(num_per_space+1):
                        nline_arr[v-1] += " "
                    num_spaces -= num_per_space
                    v -= 1
                    if v > 0:
                        num_per_space = num_spaces // v
                if len(nline_arr) == 1:
                    final_line = nline_arr[0]
                    while len(final_line) < maxWidth:
                        final_line += " "
                else:
                    final_line = "".join(nline_arr)
                lines.append(final_line)
                line = word
                wrd_cnt = 1
        while len(line) < maxWidth:
            line += " "
        lines.append(line)
        return lines