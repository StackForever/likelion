from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField() # Field는 RDB에서 column과 동일한 의미. Char, Text, DateTime type의 column이다.
    created_at = models.DateTimeField() #CharField는 짧은 텍스트 데이터를 저장할 때 사용. 최대 길이 제한 가능.
                                        #TextField는 대용량의 텍스트 데이터를 저장할 때 사용.
                                        #DateField는 날짜만 저장하고 싶을 때
                                        #DateTimeField는 날짜와 시간을 같이 저장하고 싶을 때 사용
                                        #Django 공식홈페이지의 Model Field Reference에서 모든 항목을 볼 수 있다.
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
    # 좋아요 기능과 같은 M:N 관계를 위한 중간 Table을 생성. 연결하고자 하는 모델 중 하나에 작성하면 됨.
    # posts model에 작성했으니 ManyToManyField의 첫번째 인자에 연결하고자 하는 model인 User를 작성
    image = models.ImageField(upload_to = 'posts', null = True)

    def __str__(self): #필수는 아니지만 모델을 프린트하면 model의 아이디만 출력되고 내용물을 확인할 수 없기 때문에
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        else:
            return f'{self.body}' #해당 인스턴스가 어떤 어트리뷰트를 포함하고있는지 간단히 확인할 수 있도록 추가한 것
        #Post class의 인스턴스가 출력될 때 author와 body 정보가 출력됨.

#터미널에 python manage.py makemigrations posts(app이름) 을 입력하면 migration파일이 생성됨
