class Office:
    def employee(self,sal):
        if sal<=15000:
            sal=sal+(sal*15/100)
            final_salary=sal
            print(final_salary)


f=Office()
sal=int(input('enter the salary: '))

f.employee(sal)
type(sal)
    
