'''This is a program to work out all the possible bord possisions for the 8 queens problem.
first let me explain the bord, the bored is just an 8 digit list with the numbers 1 till 8
where every number in the list is considered as a x co ordinate of a queen and every index 
of the list is considred as the y co ordinate of a queen this way each queen is ensured to be on a 
row and a differant column wich already solvse a great deal of the problem then the next
tricky bit is working out the diaginals and getting all the differant permutations of the
list because [1,2,3...] isnt exactly going to give us all the permtations'''

'''ls in this case is the name of the list containint the queen positions (i know very bad veriable naming)'''
ls = [1,2,3,4,5,6,7,8]

'''So now for wording out the diaginals. here i define a function called diag (stand for diaginal). 
WARNING! The code you are about to see is not very good as I wrote it at 1:00 am'''
def diag(ls):
    '''so we loop through every queen and call the queen1 and we compare queen1 to all the other queens
    or queen2'''
    for queen1 in ls:
        for queen2 in ls:
            #we have to make sure we are not comparing a queen to itself
            if queen1 != queen2:

                '''this if statement does all the checking but it is quite tricky to explain.
                imagine there was a diaginal going from left to right and from bottom to top
                and say that the lower of the queen was higher than the first row and further
                than the first column, what we could do is subtract the lower queens x and y 
                value from the higher queens that way we can say that the lower queens x & y 
                are at zero so the values we are left with are the x & y of the second queen 
                relitave to the first and if x & y are equal than its a diagonal.
                However sercomstances are not always so conviniant as that so we add the abs 
                force peices where we want to make to easily see if the queens are diaginal

                I hope you understood what I was talking about, it is a bit tricky to explain
                without visual aid.
                (the reason we are adding one to the ls index is because python starts counting
                from zero)'''
                if abs(queen1 - queen2) == abs((ls.index(queen1)+1) - (ls.index(queen2)+1)):

                    return True
                    # we break because if we find on diagonal then we can already scrap the permutation
                    break 
    return False


# for the final piece to the puzzle finding all the permutations the board can have in its restricted state
def board_permutations(options, current_veriation = [], all_permutations = []):
    '''Ok using recusion we will find all the permutations of the list.
    This function takes options (its called because we will use all the numbers in this list ass options later on)
    as a first argument wich is the list you want to find permutations of. The second argument is the current 
    veriation wich defualts to an empty list and the last arument all permutations wich will in the end be a list of
    all the permutations '''

    # first we define our escape case and to do so we look is the length of options is equal to one (this will make more sence later)
    if len(options) == 1:
        # so now if the length of options is one then we can just add the final number to the current veriation giving us the final veriatoin
        final_veriatoin = current_veriation + options

        #now we can emidiatly check if there are diaginals,if not we add final veriation to all permutatios and return final veriation
        #if final does have diaginals then we just return all permutations without adding any thing to it
        if not diag(final_veriatoin):
            all_permutations.append(final_veriatoin)
            return all_permutations
        else:
            return all_permutations
            
    # we loop through the lenth of optoins because it is a bit easier to use indexes
    for index in range(len(options)):
        #we make a copy of our current veriation becuase in the next loop it will be will be different and and add a number from the optoins list
        next_veriation = current_veriation[:]
        next_veriation.append(options[index])

        # now we create a new options list wich doesn't have the number we added to our current veriation
        next_options = options[:index] + options[index+1:]

        # and finally we call the function again and make it equal to all permutations
        all_permutations = board_permutations(next_options, next_veriation, all_permutations)

    # and finally after the loop we return the final veriation of all permutations
    return all_permutations

# bonus round, how to print the board out all pritty. Lets define a function called print board

def print_board(board_list):
    '''So what we will do is for every squar on the board that doesn'nt have a queen on it we will print a hash tag
    and for every squar with a queen on it we will print a Q'''
    pass

print(len(board_permutations(ls)))
