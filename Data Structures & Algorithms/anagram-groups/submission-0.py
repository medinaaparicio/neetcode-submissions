class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)  #keys are arrays and 
        for word in strs:
            key = self.buildArray(word)
            grams[tuple(key)].append(word)
        return list(grams.values())
    
    # takes in a word and returns an array where each index represents
    # the frequency of the corresponding letter in the alphabet
    def buildArray(self, word: str) -> List[int]:
        array = [0 for i in range(26)]
        for char in word:
            array[ord(char) - 97] += 1
        return array


        
        