from django.forms import ModelForm
from .models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = EMPLOYEE
        fields = ['fname', 'minit', 'lname', 'bdate', 'address', 'ssn', 'sex', 'salary', 'super_ssn', 'dno']

class DeleteEmp(ModelForm):
	field_order = ['fname', 'minit', 'lname', 'bdate', 'address', 'ssn', 'sex', 'salary', 'super_ssn', 'dno']
	class Meta:
		model = EMPLOYEE
		exclude = ['fname', 'minit', 'lname', 'bdate', 'address', 'sex', 'salary', 'super_ssn', 'dno']

class DepartmentForm(ModelForm):
	class Meta:
		model = DEPARTMENT
		fields = ['dname','dnumber','mgr_ssn','mgr_start_date']

class DeleteDep(ModelForm):
	field_order = ['dname','dnumber','mgr_ssn','mgr_start_date']
	class Meta:
		model = DEPARTMENT
		exclude = ['dname','mgr_ssn','mgr_start_date']

class Dept_locationForm(ModelForm):
	class Meta:
		model = DEPT_LOCATION
		fields = ['dnumber','dlocation']

class DeleteDL(ModelForm):
	field_order = ['dnumber','dlocation']
	class Meta:
		model = DEPT_LOCATION
		exclude = ['dlocation']

class ProjectForm(ModelForm):
	class Meta:
		model = PROJECT
		fields = ['pname','pnumber','plocation','dnum']

class DeletePro(ModelForm):
	field_order = ['pname','pnumber','plocation','dnum']
	class Meta:
		model = PROJECT
		exclude = ['pname','plocation','dnum']

class Works_onForm(ModelForm):
	class Meta:
		model = WORKS_ON
		fields = ['essn','pno','hours']

class DeleteWor(ModelForm):
	field_order = ['essn','pno','hours']
	class Meta:
		model = WORKS_ON
		exclude = ['pno','hours']

class DependentForm(ModelForm):
	class Meta:
		model = DEPENDENT
		fields = ['essn','dependent_name','sex','bdate','relationship']

class DeleteDDT(ModelForm):
	field_order = ['essn','dependent_name','sex','bdate','relationship']
	class Meta:
		model = DEPENDENT
		exclude = ['dependent_name','sex','bdate','relationship']