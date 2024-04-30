# Loops

    Syntax:
    while(condition):
        #statement

# Forloop remove unit digit
Program to remove unit digit in a number.

Example 1:

    Enter a number:4596 
    Number after removing unit digit= 459

# Forloop find unit digit
Program to find unit digit in a number.

units digit of a number is the digit in the one's place of the number. It is the rightmost digit of the number.

Example 1:

    Enter a number:545
    Unit digit in a number 5
    

# Whileloop-count-number
while loop count numbers

    # condition : Run loop till count is less than 10

      1
      2
      3
      4
      5
      6
      7
      8
      9

#  Sum of unit digit
forloop

Program to find sum of unit digit in a given number.

    Program Explanation:
    1. User must first enter the value and store it in a variable.
    2. The for loop is used and the last digit of the number is obtained by using the modulus operator.
    3. The digit is added to another variable each time the loop is executed.
    4. This loop terminates when the value of the number is 0.
    5. The total sum of the number is then printed.

Example 1:

    Enter a number:1235
    Sum= 11

Example 2:

    Enter a number:2598
    Sum= 24

Example 3:

    Enter a number:9875325
    Sum= 39

    
# Sum of digits
while loop

    Program Explanation:
    1} User must first enter the value and store it in a variable.
    2} The for loop is used and the last digit of the number is obtained by using the modulus operator.
    3} The digit is added to another variable each time the loop is executed.
    4} This loop terminates when the value of the number is 0.
    5} The total sum of the number is then printed.
    
Example 1:

    Enter a number >> 12
    Sum of digits = 3
    
Example 2:

    Enter a number >> 365
    Sum of digits = 14

# Reverse of digits
Reverse of digits

    Program Explanation:
    
    1} User must first enter the value and store it in a variable n.
    
    2} The for loop is used and the last digit of the number is obtained by using the modulus operator.
    
    3} The last digit is then stored at the one’s place, second last at the ten’s place and so on.
    
    4} The last digit is then removed by truly dividing the number with 10.
    
    5} This loop terminates when the value of the number is 0.
    
    6} The reverse of the number is then printed.

Example 1:

    Enter a number:548
    Reverse of digits= 845

Example 2:

    Enter a number:987
    Reverse of digits= 789

Example 3:
    
    Enter a number:739
    Reverse of digits= 937
    
# Product of digits
Product of digits

Example 1:

    Enter a number:4586
    Product of digits= 960

Example 2:

    Enter a number:325
    Product of digits= 30

Example 3:

    Enter a number:39
    Product of digits= 27
        
    

# Armstrong number
Armstrong number


    Program Explanation >>
    
    1} User must enter the number and store it in a variable.
    2} The map function obtains each digit from the number and converts it to a string and stores it in a list.
    3} The second map function cubes each digit and stores it in another list.
    4} Then the sum of the cubes of the digits is found and is checked if it is equal to the original number.
    5} If the sum of the cube of digits is equal to the original number, the number is an Armstrong number.
    6} The final result is printed.

Example 1:

    Enter a number:153
    Sum= 153
    It is a Armstrong number

Example 2:

    Enter a number:125
    Sum= 134
    It is not a Armstrong number

Example 3:

    Enter a number:407
    Sum= 407
    It is a Armstrong number

Example 4:

    Enter a number:469
    Sum= 1009
    It is not a Armstrong number
    
    
# Range
range

Syntax:

       for i in range(start,end):
       
           //statement
           
Program Explanation:

      * Start value included
      * end value.(Excluded)
      * I value gets auto incremented by 1 (Default)
      
Example:

    0 Python
    1 Python
    2 Python
    3 Python
    4 Python
    5 Python

# 𝐏𝐚𝐥𝐢𝐧𝐝𝐫𝐨𝐦𝐞 𝐧𝐮𝐦𝐛𝐞𝐫
𝐏𝐚𝐥𝐢𝐧𝐝𝐫𝐨𝐦𝐞 𝐧𝐮𝐦𝐛𝐞𝐫

𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧:

    The program takes a number and checks whether it is a palindrome or not.


Program Explanation:
    
    1} User must first enter the value of the integer and store it in a variable.
    2} The value of the integer is then stored in another temporary variable.
    3} The for loop is used and the last digit of the number is obtained by using the modulus operator.
    4} The last digit is then stored at the one’s place, second last at the ten’s place and so on.
    5} The last digit is then removed by truly dividing the number with 10.
    6} This loop terminates when the value of the number is 0.
    7} The reverse of the number is then compared with the integer value stored in the temporary variable.
    8} If both are equal, the number is a palindrome.
    9} If both aren’t equal, the number isn’t a palindrome.
    10} The final result is then printed.

Example 1:
    
    Enter a number: 121
    reverse= 121
    it is a Palindrome number

Example 2:

    Enter a number:984
    reverse= 489
    it is not a Palindrome number

Example 3:

    Enter a number:737
    reverse= 737
    it is a Palindrome number

Example 4:
    
    Enter a number:845
    reverse= 548
    it is not a Palindrome number
