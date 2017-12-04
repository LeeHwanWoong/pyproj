# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from .forms import *

def home(request):
    return render(request, 'home.html')

def employee(request) :
    if request.method == 'POST' and 'delete' in request.POST:
        myssn = request.POST.get('ssn')
        if(EMPLOYEE.objects.all().filter(ssn=myssn)):
            EMPLOYEE.objects.all().filter(ssn=myssn).delete()
            return redirect('/EMPLOYEE/sel')
        else:
            return redirect('/EMPLOYEE')
    elif request.method == 'POST':
        form = EmployeeForm(request.POST)
        formD = DeleteEmp(request.POST)
        if form.is_valid():
            form.save()
        else :
            myfname = request.POST.get('fname')
            myminit = request.POST.get('minit')
            mylname = request.POST.get('lname')
            mybdate = request.POST.get('bdate')
            myaddress = request.POST.get('address')
            mysex = request.POST.get('sex')
            mysalary = request.POST.get('salary')
            mysuperssn = request.POST.get('super_ssn')
            mydno = request.POST.get('dno')
            myssn = request.POST.get('ssn')

            try:
                EMPLOYEE.objects.all().filter(ssn =myssn).update(fname = myfname,minit = myminit,lname = mylname,bdate = mybdate, address = myaddress,sex = mysex,salary = mysalary,super_ssn = mysuperssn, dno = mydno)
                return redirect('/EMPLOYEE/sel')
            except:
                return redirect('/EMPLOYEE')
        return redirect('/EMPLOYEE/sel')
    else:
        form = EmployeeForm()
        formD = DeleteEmp()
        return render(request, 'employee.html', {'form': form,'formD':formD})

def employee_sel(request):
    res = []
    for s in EMPLOYEE.objects.all():
        res += [s]
    return render(request, 'employee_sel.html', {'res':res})

def department(request) :
    if request.method == 'POST' and 'delete' in request.POST:
        mypk = request.POST.get('dnumber')
        if(DEPARTMENT.objects.all().filter(dnumber=mypk)):
            DEPARTMENT.objects.all().filter(dnumber=mypk).delete()
            return redirect('/DEPARTMENT/sel')
        else:
            return redirect('/DEPARTMENT')
    elif request.method == 'POST':
        form = DepartmentForm(request.POST)
        formD = DeleteDep(request.POST)
        if form.is_valid():
            form.save()
        else :
            mydname = request.POST.get('dname')
            mydnumber = request.POST.get('dnumber')
            mymgr_ssn = request.POST.get('mgr_ssn')
            mymgr_start_date = request.POST.get('mgr_start_date')
            try:
                DEPARTMENT.objects.all().filter(dnumber=mydnumber).update(dname = mydname,dnumber = mydnumber,mgr_ssn = mymgr_ssn,mgr_start_date = mymgr_start_date)
                return redirect('/DEPARTMENT/sel')
            except:
                return redirect('/DEPARTMENT')
        return redirect('/DEPARTMENT/sel')
    else:
        form = DepartmentForm()
        formD = DeleteDep()
        return render(request, 'department.html', {'form': form,'formD':formD})

def department_sel(request):
    res = []
    for s in DEPARTMENT.objects.all():
        res += [s]
    return render(request, 'department_sel.html', {'res':res})

def dept_location(request) :
    if request.method == 'POST' and 'delete' in request.POST:
        mypk = request.POST.get('dnumber')
        if(DEPT_LOCATION.objects.all().filter(dnumber=mypk)):
            DEPT_LOCATION.objects.all().filter(dnumber=mypk).delete()
            return redirect('/DEPT_LOCATION/sel')
        else:
            return redirect('/DEPT_LOCATION')
    elif request.method == 'POST':
        form = Dept_locationForm(request.POST)
        formD = DeleteDL(request.POST)
        if form.is_valid():
            form.save()
        else :
            mydnumber = request.POST.get('dnumber')
            mydlocation = request.POST.get('dlocation')
            try:
                DEPT_LOCATION.objects.all().filter(dnumber = mydnumber).update(dnumber = mydnumber,dlocation = mydlocation)
                return redirect('/DEPT_LOCATION/sel')
            except:
                return redirect('/DEPT_LOCATION')
        return redirect('/DEPT_LOCATION/sel')
    else:
        form = Dept_locationForm()
        formD = DeleteDL()
        return render(request, 'dept_location.html', {'form': form,'formD':formD})

def dept_location_sel(request):
    res = []
    for s in DEPT_LOCATION.objects.all():
        res += [s]
    return render(request, 'dept_location_sel.html', {'res':res})

def project(request) :
    if request.method == 'POST' and 'delete' in request.POST:
        mypk = request.POST.get('pnumber')
        if(PROJECT.objects.all().filter(pnumber=mypk)):
            PROJECT.objects.all().filter(pnumber=mypk).delete()
            return redirect('/PROJECT/sel')
        else:
            return redirect('/PROJECT')
    elif request.method == 'POST':
        form = ProjectForm(request.POST)
        formD = DeletePro(request.POST)
        if form.is_valid():
            form.save()
        else :
            mypname = request.POST.get('pname')
            mypnumber = request.POST.get('pnumber')
            myplocation = request.POST.get('plocation')
            mydnum = request.POST('dnum')
            try:
                PROJECT.objects.all().filter(pnumber = mypnumber).update(pname = mypname, plocation = myplocation,dnum = mydnum)
                return redirect('/PROJECT/sel')
            except:
                return redirect('/PROJECT')
        return redirect('/PROJECT/sel')
    else:
        form = ProjectForm()
        formD = DeletePro()
        return render(request, 'project.html', {'form': form,'formD':formD})

def project_sel(request):
    res = []
    for s in PROJECT.objects.all():
        res += [s]
    return render(request, 'project_sel.html', {'res':res})

def works_on(request) :
    if request.method == 'POST' and 'delete' in request.POST:
        mypk = request.POST.get('essn')
        if(WORKS_ON.objects.all().filter(essn=mypk)):
            WORKS_ON.objects.all().filter(essn=mypk).delete()
            return redirect('/WORKS_ON/sel')
        else:
            return redirect('/WORKS_ON')
    elif request.method == 'POST':
        form = Works_onForm(request.POST)
        formD = DeleteWor(request.POST)
        if form.is_valid():
            form.save()
        else :
            myessn = request.POST.get('essn')
            mypno = request.POST.get('pno')
            myhours = request.POST.get('hours')

            try:
                WORKS_ON.objects.all().filter(essn =myessn).update(essn = myessn, pno = mypno, hours=myhours)
                return redirect('/WORKS_ON/sel')
            except:
                return redirect('/WORKS_ON')
        return redirect('/WORKS_ON/sel')
    else:
        form = Works_onForm()
        formD = DeleteWor()
        return render(request, 'works_on.html', {'form': form,'formD':formD})

def works_on_sel(request):
    res = []
    for s in WORKS_ON.objects.all():
        res += [s]
    return render(request, 'works_on_sel.html', {'res':res})

def dependent(request) :
    if request.method == 'POST' and 'delete' in request.POST:
        mypk = request.POST.get('essn')
        if(DEPENDENT.objects.all().filter(essn=mypk)):
            DEPENDENT.objects.all().filter(essn=mypk).delete()
            return redirect('/DEPENDENT/sel')
        else:
            return redirect('/DEPENDENT')

    elif request.method == 'POST':
        form = DependentForm(request.POST)
        formD = DeleteDDT(request.POST)
        if form.is_valid():
            form.save()
        else :
            myessn = request.POST.get('essn')
            mydependent_name = request.POST.get('dependent_name')
            mysex = request.POST.get('sex')
            mybdate = request.POST.get('bdate')
            myrelationship = request.POST.get('relationship')
            try:
                DEPENDENT.objects.all().filter(essn =myessn).update(essn = myessn, dependent_name = mydependent_name, sex=mysex, bdate= mybdate, relationship = myrelationship)
                return redirect('/DEPENDENT/sel')
            except:
                return redirect('/DEPENDENT')
        return redirect('/DEPENDENT/sel')
    else:
        form = DependentForm()
        formD = DeleteDDT()
        return render(request, 'dependent.html', {'form': form,'formD':formD})

def dependent_sel(request):
    res = []
    for s in DEPENDENT.objects.all():
        res += [s]
    return render(request, 'dependent_sel.html', {'res':res})

def init(request)   :
    EMPLOYEE.objects.all().delete()
    DEPARTMENT.objects.all().delete()
    DEPT_LOCATION.objects.all().delete()
    PROJECT.objects.all().delete()
    WORKS_ON.objects.all().delete()
    DEPENDENT.objects.all().delete()

    emp1 = EMPLOYEE(fname = 'John',minit = 'B',lname = 'Smith', bdate = '1965-01-09',address = '731 Fondren,Houston,TX',ssn =123456789,sex = 'M',salary = 30000 ,super_ssn = 333445555 ,dno = 5)
    emp1.save()
    emp2 = EMPLOYEE(fname = 'Franklin',minit = 'T',lname = 'Wong',bdate = '1955-12-08',address = '638 Vose, Houston, Tx',ssn =33344555,sex = 'M',salary = 40000 ,super_ssn = 888665555,dno = 5)
    emp2.save()
    emp3 = EMPLOYEE(fname = 'Alicia',minit = 'J',lname = 'Zelaya',bdate = '1968-01-19',address = '3321 Castle, Spring, TX',ssn =999887777,sex = 'F',salary = 25000,super_ssn = 987654321 ,dno = 4)
    emp3.save()

    works_on1 = WORKS_ON(essn = 123456789, pno = 1, hours = 32.5)
    works_on1.save()
    works_on2 = WORKS_ON(essn = 666884444, pno = 3, hours = 40)
    works_on2.save()
    works_on3 = WORKS_ON(essn = 453453453, pno = 1, hours = 20)
    works_on3.save()

    dep1 = DEPARTMENT(dname = 'Research',dnumber = 5,mgr_ssn = 333445555,mgr_start_date = '1988-05-22')
    dep2 = DEPARTMENT(dname = 'Administration',dnumber = 4,mgr_ssn = 987654321,mgr_start_date = '1995-01-01')
    dep3 = DEPARTMENT(dname = 'Headquarters',dnumber = 1,mgr_ssn = 888665555,mgr_start_date = '1981-06-19')
    dep1.save()
    dep2.save()
    dep3.save()

    depl1 = DEPT_LOCATION(dnumber = 1,dlocation = 'Houston')
    depl2 = DEPT_LOCATION(dnumber = 4,dlocation = 'Stafford')
    depl3 = DEPT_LOCATION(dnumber = 5,dlocation = 'Bellaire')
    depl1.save()
    depl2.save()
    depl3.save()

    pro1 = PROJECT(pname = 'ProductX',pnumber = 1,plocation = 'Bellaire',dnum = 5)
    pro2 = PROJECT(pname = 'ProductY',pnumber = 2,plocation = 'Sugarland',dnum = 5)
    pro3 = PROJECT(pname = 'ProductZ',pnumber = 3,plocation = 'Houston',dnum = 5)
    pro1.save()
    pro2.save()
    pro3.save()

    ddt1 = DEPENDENT(essn = 333445555,dependent_name = 'Alice',sex = 'F',bdate = '1986-04-05',relationship = 'Daughter')
    ddt2 = DEPENDENT(essn = 987654321,dependent_name = 'Abner',sex = 'M',bdate = '1942-02-28',relationship = 'Spouse')
    ddt3 = DEPENDENT(essn = 123456789,dependent_name = 'Michael',sex = 'M',bdate = '1988-01-04',relationship = 'Son')
    ddt1.save()
    ddt2.save()
    ddt3.save()


    return render(request, 'init.html')