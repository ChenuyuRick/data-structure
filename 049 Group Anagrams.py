class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            word_sorted = ''.join(sorted(word))
            if word_sorted not in dic:
                dic[word_sorted] = [word]
            else:
                dic[word_sorted].append(word)
        output = []
        for key in dic.keys():
            output.append(dic[key])
        return output
