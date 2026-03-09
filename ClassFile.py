class MultiFunc():
        def Subfields():
            sub_ai_list = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
            print('Sub-fields in AI are:')
            for subai in sub_ai_list:
                print(subai)
                
        def OddEven():
            num = int(input('Enter a number: '))
            if (num%2==0):
                print(num, 'is Even number')
            else:
                print(num, 'is Odd number')
                
        def Elegible():
            Gender = input('Your Gender: ')
            Age = int(input('Your Age: '))
            if (Gender == 'Male'):
                      if (Age < 21):
                        print('Not Eligible')
                      else:
                        print('Eligible')
            elif (Gender == 'Female'):
                      if (Age < 18):
                        print('Not Eligible')
                      else:
                        print('Eligible')
                          
        def percentage():
            sub1=int(input('Subject1: '))
            sub2=int(input('Subject2: '))
            sub3=int(input('Subject3: '))
            sub4=int(input('Subject4: '))
            sub5=int(input('Subject5: '))
            Total = sub1 + sub2 + sub3 + sub4 + sub5
            print('Total: ', Total)
            Percentage = Total/5
            print('Percentage: ',Percentage)
    
        def triangle():
            Height = int(input('Height: '))
            Breadth = int(input('Breadth: '))
            print('Area formula: (Height*Breadth)/2')
            Area = (Height*Breadth)/2
            print('Area of Triangle: ',Area)
            Height1 = int(input('Height1: '))
            Height2 = int(input('Height2: '))
            Breadth = int(input('Breadth: '))
            print('Perimeter formula: Height1+Height2+Breadth')
            Perimeter = Height1+Height2+Breadth
            print('Perimeter of Triangle: ', Perimeter)
    
    
