"""WriteaPythonfunctionbasic salarythataccepts twoparameters: hourly rateandhours worked per week.
 Thefunction should calculate the basic salary per month (assuming a month has 4 weeks). If the hours
 worked per week exceed 40, create another function overtime salary, where every extra hour worked
 is paid at 1.5 times the normal hourly rate. Finally, create another function total salary that returns
 the sum of the basic salary and overtime."""

def basic_salary(h_r,hpw):          #hourly rate,hours per week
    if(0<=hpw<=40):
        return h_r*hpw*4
    elif(hpw>40):
        ot=hpw-40                   #overtime per work
        ots=overtime_salary(h_r,ot)   #overtime Salary
        bs=h_r*40*4
        return total_salary(bs,ots)
    else:
        return -1

def overtime_salary(h_r,eh):  #hourly rate, extra hours
    return (h_r*1.5)*eh*4
def total_salary(bs,ots):    # basic salary, overtime Salary
    return bs+ots

def tax_amount(bs):
    if(bs>=85000):
        return .2*bs
    elif(bs>=60000):
        return .15*bs
    else:
        return .1*bs

def gross_salary(bs):
    all=.2
    ta=tax_amount(bs)
    if(ta>=0):
        return bs+(.2*bs)-ta
    else:
        return -1
def salary_bracket(gs):
    if(gs>=80000):
        print("High Income")
    elif(gs>=50000):
        print("Middle Income")
    elif(gs>=0):
        print("Low Income")
    else:
        print("Invalid")
i=3
emp={}
while(i>0):
    ename=input("Enter Employee name: Mr./Mrs. ")
    hpw=int (input("Enter Hours Worked per Week: "))
    hr=float(input("Enter Hourly Rate: Rs."))
    emp[i]=[ename,hpw,hr]
    i-=1
print("Employee Name\tBasic Salary\tTotal Salary\tGross Salary\tTax Amount\tSalary Bracket")
for i in emp:
    print(emp[i][0],end="\t")
    print(basic_salary(emp[i][2],emp[i][1]),end="\t")
    #print(emp[i][0],end="\t")
    

