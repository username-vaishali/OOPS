####Class block to collect the data attribute and process

# def display(obj):
#   print(obj.name)

# class Company:
#     rooms=20
#     chairs=50
#     Acs=15

    ### Methods

    # def __init__(self,name=None,course=None,loc=None):
    #   self.name=name
    #   self.course=course
    #   self.loc=loc
    #   print("name of student: ",self.name)
 
      # print("Constructor calling")
      

    # def training(self):
    #   obj=Company()
    #  self.name=name  #new attribute design
      # obj.name=self.name.upper()
    # #  print("this is training") 
    #   obj.course=self.course.upper()
    #   obj.loc= self.loc.upper()
      # return obj

    # def certification(self):
    #   print("name of student: ",self.name)  
    #   print("this is certification")   
    #   print("no, of room:",self.rooms)

### Object:-  instance of a class to access the class attributs and methods

# a=Company("vashi","python","delhi")
# display(a)
# b=Company()
# b=a.training()
# print(a.name)
# print(a.course)
# print(a.loc)
# a.certification()
# a.rooms=30
# print(a)
# print(a.rooms)
# print(Company().chairs)
# print(Company().rooms)
# print(b.Acs)

## Constructor  --- Method

############### Properties of an objectes

## Object created by class calling 
     # a=Company()

## object can be copied
  # c=a
  # a.rooms= 30
  # print(c.rooms)

## Can delete any object
  # del a
  # print(a.rooms)

  ## object can be passed as argument                   Problem............................

  ## object can be returnned from method                  " " " "  " "



  ############ Features of objects
  #inheritance 
  #polymorphism
  #abstruction
  #encapsulation


  #------------inheritance(natively,heridity) 
  # 1.single inheritance
# class Base:
#   a=10

# class Derived(Base):
#   pass


# d=Derived()
# print(d.a)

# 2. multiple inheritance

# class Base1:
#   a=10
# class Base2:
#   b=20
# class Derived(Base1,Base2):
#   pass

# d=Derived()
# print(d.a)
# print(d.b)

# 3. multilevel inheritance

# class Base1:
#   a=10

# class Derived1(Base1):
#   b=20
# class Derived2(Derived1):  
#   pass


# d=Derived2()
# print(d.a)
# print(d.b)


# 4. heirarichal inheritance

# class Base1:
#   a=10

# class Derived1(Base1):
#   pass

# class Derived2(Base1):  
#   pass


# d2=Derived2()
# print(d2.a)
# d1=Derived1()
# print(d1.a)


# 5.hybrid inheritance


# --------------polymorphism(many foam)

# method  overloading
# """    overriding
# operator overloading


# ----overloading




# class calc:
#   def add(self,a,b):
#     self.a=a
#     self.b=b
#     return self.a + self.b


# c=calc()
# print(c.add())
# print(c.add(3))
# # print(c.add(5,7))

# ----overriding

# class base:
#   def method1(self):
#     print("method calling")
# class Derived1(base):
#   def method1(self):
#     print("method 1 calling in derived class")


# d=Derived1()
# d.method1()    
  
# -----operator overloading
class calc:
  def __init__(self):
    self.a=a
  def __add__(self,other): 
    return self.a+other.a

c1=calc(6)
# print(c1.__add__(7))
c2=calc(8)

print(c1+c2)



# ------------------encapsulation
# # acess modification
##public
##protected
##private


# ----------public

# class company:
#   def __init__(self,name=None,course=None,loc=None):
#     self.name=name
#     self._course=course     # protecte
#     self.__loc=loc           #public
#   def display_info(self):
#     print("nmae",self.name)
#     print("course",self._course)
#     print("location:",self.__loc)
#   def update_loc(self,new__loc):
#     self.__loc=new__loc


# s1=company("rohit","java","noida")
# s1.display_info()      
# print(s1.name)
# print(s1._course)
# print(s1.__loc)
# s1.update_loc()

# abstaration---------
# from abc import ABC,abstractmethod
# class Vehicle(ABC):   #hide property
#   @abstractmethod  #function in argument pass
#   def start(self):
#     print("vehicle star method")
#   def stop(self):
#     print("stop method")
#   def run(self):
#     print("run method")

# class Car(Vehicle):
#   def start():
#     print("car method")

# c=car()
# c.start()
# c.stop()
# c.run()

######  modules and package
# import function as func    ## as use secondary name

# from function import fact,repete
# from Function import *  # all classes define

# print(func.fact(6))
# print(fact(5))
# repete()
# from user_package.collection import sqaure_list
# print(sqaure_list([3,5,1,2]))


#### METHOD.......................................

##Static Method
#class Method


# class calc:

#   def __init__(self,a,b):
#     self.a=a
#     self.b=b

#   def add(self):
#       return self.a+self.b

#   @staticmethod
#   def iseven(x):
#     if x%2==0:
#       return True
#     else:
#       return False

# c=calc(6,4)
# print(c.add())
# print(c.iseven(6))


### Class Method.........................................................


# class empinfo:

#      def __init__(self,name, age,loc):
#       self.name=name
#       self.age=age
#       self.loc=loc

#      @classmethod
#      def info_by_birthyear(self,name,birthyear,loc):
#       return self(name,2022-birthyear,loc)

#      def disp_info(self,):
#       print("employe name:", self.name)
#       print("employe age",self.age)
#       print("employe location:", self.loc)

# # c=empinfo("vashi", 21, "delhi")
# a=empinfo.info_by_birthyear("vashi",1999,"mzn")
# a.disp_info()



    


    












