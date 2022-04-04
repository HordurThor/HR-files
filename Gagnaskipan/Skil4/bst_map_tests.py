from bst_map import *

def test_map(m):
    try:
        m.insert(5, "fimma")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(4, "fjarri")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(2, "tvistur")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(5, "fimmarimma")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(1, "ás")
    except ItemExistsException:
        print("Item already exists")

    try:
        m.update(4, "fjarkalarki")
    except NotFoundException:
        print("Item not found")
    try:
        m.update(6, "sexxxxxa")
    except NotFoundException:
        print("Item not found")

    try:
        m.insert(6, "sexa")
    except ItemExistsException:
        print("Item already exists")

    print("size of map: " + str(len(m)))
    print(m.contains(12))
    try:
        m.insert(12, "drolla")
    except ItemExistsException:
        print("Item already exists")
    print(m.contains(12))

    print("size of map: " + str(len(m)))
    try:
        print(m.find(4))
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(2))
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(1))
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(5))
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(6))
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(7))
    except NotFoundException:
        print("Item not found")

    print("size of map: " + str(len(m)))
    try:
        m.remove(5)
        print("Item removed")
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(5))
    except NotFoundException:
        print("Item not found")
    try:
        m.remove(5)
        print("Item removed")
    except NotFoundException:
        print("Item not found")
        
    print("size of map: " + str(len(m)))

    print(m)
    
    try:
        m.update(12, "drolla")
    except NotFoundException:
        print("Item not found")
    print(m)

    try:
        m.insert(6, "sixxer")
    except ItemExistsException:
        print("Item already exists")
    print(m)

    try:
        m.insert(9, "nía")
    except ItemExistsException:
        print("Item already exists")
    print(m)


if __name__ == "__main__":
    print("\nTESTING BSTMAP")
    m = BSTMap()
    test_map(m)
    