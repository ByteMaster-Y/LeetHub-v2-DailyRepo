class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        
        # 슬라이딩 윈도우
        start = 0
        max_len = 0

        # 문자열 끝까지 중복 확인
        for end in range(len(s)):
           # 중복이 발생하면, start 포인터를 이동시켜 중복을 해결
           while s[end] in char_set:
                char_set.remove(s[start]) 
                start += 1 
        
           # 중복 해결 후, 현재 end 문자를 Set에 추가하여 윈도우를 확장합니다.
           char_set.add(s[end])
                
           # 최대 길이 갱신
           max_len = max(max_len, end - start + 1)

        return max_len