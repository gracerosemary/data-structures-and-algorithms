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
        

# code review
def merge_list(ll1, ll2):
    # validate that both lists have nodes

    current_ll1 = ll1.head
    current_ll2 = ll2.head

    while current_ll1 and current_ll2:
    
        ll1_next = current_ll1.next
        ll2_next = current_ll2.next

        current_ll1.next = current_ll2

        # do a check for ll1_next. if none, break or return
        if not ll1_next:
            break
        
        current_ll2.next = ll1_next 

        current_ll1, current_ll2 = ll1_next, ll2_next

    return ll1
