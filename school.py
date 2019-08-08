class School:
    
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster        
     
    def add_student(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade
        
        result = self.roster.get(student_grade, 'No')
        
        if result == 'No':
            self.roster[student_grade] = []
            self.roster[student_grade].append(student_name)
        
        else:
            self.roster[student_grade].append(student_name)   
    
    def grade(self, student_grade):
        
        return self.roster[student_grade]
   

    def sort_roster(self):
        
        for i in list(self.roster.keys()):
            self.roster[i].sort()
        return self.roster
      
 
     
        