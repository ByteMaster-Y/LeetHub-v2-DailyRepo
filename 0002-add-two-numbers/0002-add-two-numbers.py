# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 새로운 결과 리스트의 시작점을 지정할 더미 헤드 노드를 만든다 값은 0으로!
        dummy_head = ListNode(0)

        current_result = dummy_head

        # 자리 올림수
        carry = 0

        while l1 is not None or l2 is not None or carry !=0 :
            # 값 추출
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total_sum = val1 + val2 + carry

            # 자리 올림 수 계산
            carry = total_sum // 10

            new_val = total_sum % 10

            # 새 노트 생성 및 연결
            # new_val을 값으로 가지는 새 노드를 만들고, 현재 결과 리스트의 다음 노드에 연결한다.
            current_result.next = ListNode(new_val)

            current_result = current_result.next

            # l1, l2 포인터 이동
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy_head.next
