def open_file(input_file):
    with open(input_file) as f:
        lines = f.readlines()
    return lines

def extract_lists(input_file):
    listA = []
    listB = []
    for line in input_file:
        line = line.split()
        listA.append(int(line[0]))
        listB.append(int(line[1]))
    return listA, listB

def sort_lists(listA, listB):
    listA.sort()
    listB.sort()
    return listA, listB

def calculate_distance(listA, listB):
    distance = 0
    for i in range(len(listA)):
        distance += abs(listA[i] - listB[i])
    return distance

def score_similarity(listA, listB):
    score = 0
    for num in listA:
        occurence = listB.count(num)
        score += num * occurence
    return score


def main():
    input_file = "day1_1.txt"
    lines = open_file(input_file)
    listA, listB = extract_lists(lines)
    sorted_listA, sorted_listB = sort_lists(listA, listB)
    #question1
    #distance = calculate_distance(sorted_listA, sorted_listB)
    #print(distance)
    #question2
    score = score_similarity(sorted_listA, sorted_listB)
    print(score)

if __name__ == "__main__":
    main()