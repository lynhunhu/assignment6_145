import LList as L

def test_integration_remove_from_back_get_index_of_value_1():
    thellist = L.LList()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        thellist.append(word)
    for i in range(4):
        thellist.remove_from_back()
    print(thellist.get_index_of_value("TURN-AROUND"))
    assert thellist.get_index_of_value("TURN-AROUND") == (False, None), "TURN-AROUND should be gone"
    
test_integration_remove_from_back_get_index_of_value_1()

def test_remove_from_back_multiple_in_ref_head_2():
    thetail = L.node(29)
    thehead = L.node(33, thetail)
    thellist = L.LList()
    thellist._size = 2
    thellist._head = thehead
    thellist._tail = thetail

    flag, val = thellist.remove_from_back()
    result = thellist._head
    assert result is thehead, 'remove_from_back() on LList with 2 nodes; head should not have changed'

test_remove_from_back_multiple_in_ref_head_2()