class Student:

   def __init__(self,name,age,tracks,score):
       self.name=name
       self.age=age
       self.tracks=tracks
       self.score=score
       pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Peter=Student(name="Peter", age=34,tracks=["UI/UX"],score=20.90
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
