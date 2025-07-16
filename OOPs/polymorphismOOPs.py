# # to mimic or show logic of polymorphism
# class India:
#     def capital(self):
#         print("New Delhi")
#
# class America:
#     def capital(self):
#         print("Wahington DC")
#
# objInd = India()
# objAmerica = America()
# # capital function being polymorphic in nature
# objInd.capital() # Same Function printing Newdelhi here
# objAmerica.capital() # Same Function printing WashingtonDC here

'''To achieve polymorphism we need to make sure that there are minimum two same name functions either in the 
same class or in *2 different class* (*condition applied)'''

class Mom:
    def cook(self):
        print("Indian")

class Daughter(Mom):
    def cook(self):
        print("Chinese")

a=Mom()
b=Daughter()

a.cook()
b.cook()

