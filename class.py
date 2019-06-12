# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:43:45 2019

@author: 严军
"""
import datetime

class User:
    def __init__(self,full_name,birthday):
        name_splits=full_name.split(' ')
        self.first_name=name_splits[0]
        self.last_name=name_splits[-1]
        self.name=full_name
        self.birthday=birthday
    
    def age(self):
        birthday_splits=self.birthday.split('-')
        birthday_year=int(birthday_splits[0])
        birthday_month=int(birthday_splits[1])
        birthday_day=int(birthday_splits[2])
        
        today=datetime.date(2020,1,1)
        
        birthdate=datetime.date(birthday_year,birthday_month,birthday_day)
        print(type(today))
        print(type(birthdate))
        print(type(today-birthdate))
        
        how_old_days=(today-birthdate).days
        print(how_old_days/365)
        print((how_old_days%365)/12)
        print((how_old_days%365)%12)
        
        
        age_years=int(how_old_days/365)
        age_months=int((how_old_days%365)/12)
        age_days=(how_old_days%365)%12
        
        '''
        today_splits=today.split('-')
        year=int(today_splits[0])
        month=int(today_splits[1])
        day=int(today_splits[2])
        
        age_years=year-birthday_year
        age_months=month-birthday_month
        age_days=day-birthday_day
        '''
        return(str(age_years)+'years'+str(age_months)+'month'+str(age_days)+'day')
        
user1=User('William Ace','2001-10-13')
print(user1.first_name,user1.last_name,user1.birthday)
print(user1.age())



'''
user1=User()
user1.first_name='William'
user1.last_name='Ace'
user1.age=18

user2=User()
user2.first_name='Marry'
user2.last_name='Emma'
user2.occupation='Actor'

print(user1.first_name +' '+user1.last_name)
print(user1.first_name,user1.last_name,user1.age)
print(user2.first_name,user2.last_name,user2.occupation)
'''