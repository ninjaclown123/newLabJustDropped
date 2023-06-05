class Employee:
    def __init__(self,name,age,id,department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department


class EMS:
    def __init__(self):
        self.data = []

    def add_emp(self,employee):
        # self.data.append(employee)
        return None


    def show_employees(self):
        for i in self.data:
            print(i.name,i.id,i.age,i.department)

    def get_employee(self,id):
        found = None
        for i in range(len(self.data)):
            if self.data[i].id == id:
                found = self.data[i]
                return found
            
        raise Exception("Employee does not exist.")
        

    def delete_employee(self,id):
        found = None
        for i in range(len(self.data)):
            if self.data[i].id == id:
                found = id
                del self.data[i]
                print('employee ' + str(found) + ' was found and deleted.')
                return True
        
        raise Exception("Employee Not Found")

            
        


