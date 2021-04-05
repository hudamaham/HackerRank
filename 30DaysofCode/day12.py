

class Student(Person):

    def __init__(self,firstName,lastName,idNumber,scores):
        super().__init__(firstName,lastName,idNumber)
        self.scores=scores
    def calculate(self):
        a=sum(self.scores)/len(scores)
        if(a>=90 and a<=100):
            return 'O'
        elif(a>=80 and a<90):
            return 'E'
        elif( a>=70 and a<80):
            return 'A'
        elif ( a>=55 and a<70):
            return 'P'
        elif( a>=40 and a<55):
            return 'D'
        else:
            return 'T'
    
    
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

