

class User:
    
    def __init__(self, id, name):
        print("클래스가 생성될때 생성되는 생성자 입니다.") # mean is initialized
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0 
        
    def follow(self, user):
        user.followers += 1
        self.following += 1 
           

user_1 = User('001', ' john Doe') # 파라미터는 생성자의 순서와 똑같이 들어간다. # 명시적으로도 지정 가능함
user_2 = User('002', ' jain Doe') #

'''
또한 아래 처럼 개별 속성을 지정하여 생성도 가능하다.
'''
# user_1 = User()
# user_1.id = '001'
# user_1.name = 'john Doe'
# print(user_1.name) user_1.속성 명 을 명시하여 이를 처리할수 있다.
# print(user_1)

user_1.follow(user_2)

print(user_1.followers)
print(user_2.followers)