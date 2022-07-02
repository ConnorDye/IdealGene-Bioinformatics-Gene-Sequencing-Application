from re import I
import sys



#ACGAT
# TACGCA
# x A C G T -
# A 1 0 0 0 0
# C 0 1 0 0 0
# G 0 0 1 0 0
# T 0 0 0 1 0
# - 0 0 0 0 0

class box:
    def __init__(self, score, string1, string2) -> None:
        self.score = score
        self.string1 = string1
        self.string2 = string2

    def print(self, i:int, j:int) -> None:
        print("Box at index (", i, ",", j, ") has the following attributes: ")
        print("score: ", self.score)
        print("string1: ", self.string1)
        print("string2: ", self.string2)



def sequence(x_string:str, y_string:str, scoring_matrix:int):
    
    table_columns = len(x_string) + 1 #dimensions of the table
    table_rows = len(y_string) + 1
    solution_table = [[box(0, "", "") for x in range(table_columns)] for y in range(table_rows)] 
    # print((solution_table[0][0]).string1)
    # print(solution_table)
    
    #initialize first column
    char_index = 0
    column = 0 #i
    for row in range(table_rows): #j
        if row > 0:
            append_string1 = (solution_table[row - 1][column]).string1
            append_string2 = (solution_table[row - 1][column]).string2
        # else:
        #     append_string1 = ""
        #     append_string2 = ""
            box_to_edit = solution_table[row][column]
            # box_to_edit.score = 0
            box_to_edit.string1 = append_string1 + "-"
            box_to_edit.string2 = append_string2 + y_string[char_index]
            box_to_edit.score = solution_table[row - 1][column].score + getScore(chr(45), y_string[char_index], scoring_matrix)
            # print(solution_table[row][column].print(row, column))
            char_index = char_index + 1

    #initialize first column
    char_index = 0
    row = 0 
    for column in range(table_columns): 
        if column > 0:
            append_string1 = (solution_table[row][column-1]).string1
            append_string2 = (solution_table[row][column-1]).string2
            box_to_edit = solution_table[row][column]
            # box_to_edit.score = 0
            box_to_edit.string2 = append_string2 + "-"
            box_to_edit.string1 = append_string1 + x_string[char_index]
            box_to_edit.score = solution_table[row][column-1].score + getScore(x_string[char_index], chr(45), scoring_matrix)
            # print(solution_table[row][column].print(row, column))
            char_index = char_index + 1


    column = 1 #USED TO BE i WRONG
    while column <  table_columns: #(table_x - 1):
        row = 1
        while row < table_rows:
            x_str_index = column - 1
            y_str_index = row - 1
            diag_score = solution_table[row-1][column-1].score + getScore(x_string[x_str_index], y_string[y_str_index], scoring_matrix)
            # print("left score is ", x_string[x_str_index], "-")
            # print(getScore(x_string[x_str_index], "-", scoring_matrix))
            left_score = solution_table[row][column - 1].score + getScore(x_string[x_str_index], chr(45), scoring_matrix)
            up_score = solution_table[row - 1][column].score + getScore(chr(45), y_string[y_str_index], scoring_matrix)
    
            max_score = max(diag_score, left_score, up_score)
            # print("diag: ", diag_score, "left_score", left_score, "up_score", up_score)
            if(max_score == diag_score):
                #if you take the diagnol neighbor then you simply append x_string[x_str_index] to current box string 1
                # repeat this for y_string 
                # solution_table[i-1][j-1].print(i-1, j-1)
                solution_table[row][column].score = diag_score
                solution_table[row][column].string1 = solution_table[row-1][column-1].string1 + x_string[x_str_index]
                solution_table[row][column].string2 = solution_table[row-1][column-1].string2 + y_string[y_str_index]
            elif(max_score == left_score):
                solution_table[row][column].score = left_score
                solution_table[row][column].string1 = solution_table[row][column - 1].string1 + x_string[x_str_index]
                solution_table[row][column].string2 = solution_table[row][column - 1].string2 + "-"
            elif(max_score == up_score):
                solution_table[row][column].score = up_score
                solution_table[row][column].string1 = solution_table[row - 1][column].string1 + "-"
                solution_table[row][column].string2 = solution_table[row - 1][column].string2 + y_string[y_str_index]
            
            # solution_table[row][column].print(row,column)
            row = row + 1  
        column = column + 1
    
    # if(solution_table[table_rows - 1][table_columns - 1].score == 38):
    #     solution_table[table_rows - 1][table_columns - 1].score = 40
    # print(" ".join(solution_table[table_rows - 1][table_columns - 1].string1))
    print("x:", " ".join(solution_table[table_rows - 1][table_columns - 1].string1) )
    print("y:", " ".join(solution_table[table_rows - 1][table_columns - 1].string2) )
    print("Score:", solution_table[table_rows - 1][table_columns - 1].score)




def getScore(letter1:str, letter2:str, scoring_matrix)  -> int:
    #define indices to access scor
    i = 0
    j = 0

    if letter1 == "A":
        i = 1
    if letter1 == "C":
        i = 2
    if letter1 == "G":
        i = 3
    if letter1 == "T":
        i = 4
    if letter1 == chr(45):
        i = 5

    if letter2 == "A":
        j = 1
    if letter2 == "C":
        j = 2
    if letter2 == "G":
        j = 3
    if letter2 == "T":
        j = 4
    if letter2 == chr(45):
        j = 5

    
    return (int)(scoring_matrix[i][j])
    

def main():
    filename = sys.argv[1]
    readfile = open(filename, "r")
    scoring_matrix = []
    string1 = readfile.readline().rstrip()
    string2 = readfile.readline().rstrip()
    for x in readfile:
        lines = x.rstrip("\n").split(" ")
        scoring_matrix.append(lines)

    sequence(string1, string2, scoring_matrix)
    
main()
