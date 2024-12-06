with open("day5_1.txt") as f:
    example = f.read()

sections = example.split('\n')

page_order = []
for line in sections:
    if '|' in line:
        num1, num2 = line.split('|')
        page_order.append((int(num1), int(num2)))

pages_to_produce = []
for line in sections:
    if ',' in line:
        numbers = [int(x) for x in line.split(',')]
        pages_to_produce.append(numbers)

def get_index(number,list):
    if number not in list:
        return None
    else:
        index = list.index(number)
        return index

#to_produce = [75,47,61,53,29]
#to_produce = [75,97,47,61,53]
#print(type(to_produce))
correctly_ordered = True
middle_number_score = 0
for list in pages_to_produce:
    for number in list:
        #print(number)
        for tuples in page_order:
            primary, secondary  = tuples[0], tuples[1]
            if number == primary :
                primary_index = get_index(number, list)
                secondary_index = get_index(secondary, list)
                if secondary_index is not None and primary_index > secondary_index:
                    #print(f"number {number} has a bigger index than the secondary number {secondary} of {tuples}")
                    correctly_ordered = False
                    continue
    if correctly_ordered == True:
        middle_item = list[len(list) // 2]
        middle_number_score += middle_item
        print(f"middle item {middle_item} of {list}")
        print(f"correctly ordered list: {list}")


print(middle_number_score)

            