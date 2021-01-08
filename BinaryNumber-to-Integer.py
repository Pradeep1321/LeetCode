def getDecimalValue(head):
    stg = ''
    while head:
        stg += str(head.val)
        head = head.next
    return int(stg, 2)