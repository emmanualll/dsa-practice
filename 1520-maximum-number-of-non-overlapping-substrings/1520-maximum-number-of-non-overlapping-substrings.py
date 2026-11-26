class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            
            last[char] = i

        intervals = []

        for char in first:

            start = first[char]
            end = last[char]

            i = start
            valid = True

            while i <= end:
                current = s[i]

                if first[current] < start:
                    valid = False
                    break
                
                end = max(end, last[current])

                i += 1
            if valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: (x[1], -x[0]))

        result = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end

        return result

        