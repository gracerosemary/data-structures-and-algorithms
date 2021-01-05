def zipLists(list1, list2):
    list1_current = list1.head
    list2_current = list2.head

    while list1_current and list2_current:
        temp1 = list1_current.next
        temp2 = list2_current.next

        list1_current.next = list2_current
        list2_current.next = temp1

        list1_current = temp1
        list2_current = temp2
    return list1
        

