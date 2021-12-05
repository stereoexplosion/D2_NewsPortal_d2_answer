from news.models import *

User.objects.create_user('Vladimir')
User.objects.create_user('Mark')

a1 = Author.objects.create(author=User.objects.get(username='Vladimir'))
a2 = Author.objects.create(author=User.objects.get(username='Mark'))

c1 = Category.objects.create(category_name='Спорт')
c2 = Category.objects.create(category_name='Наука')
c3 = Category.objects.create(category_name='Политика')
c4 = Category.objects.create(category_name='Экономика')

p1 = Post.objects.create(author=Author.objects.get(id=1), post_choice='AR', post_heading='Кипр чемпион мира по футболу!', post_text='wertyuiopsadfghjsadfasskhdbfchlkashbdlahsbdo')
ca1 = Category.objects.get(id=1)
p1.category.add(ca1)

>>> p2 = Post.objects.create(author=Author.objects.get(id=2), post_choice='NE', post_heading='Биткоин обновил исторический максимум!', post_text='nwoisfdbvnaopisjndfpasjndfpijasndpifjnasdijfnbasdjnfoiasjndfpasijndfadsnsd')
>>> ca2=Category.objects.get(id=4)
>>> p2.category.add(ca2)
>>> ca4 = Category.objects.get(id=3)
>>> p2.category.add(ca4)

>>> p3 = Post.objects.create(author=Author.objects.get(id=2), post_choice='AR', post_heading='Открыт новый элемент химической таблицы!', post_text='uapdfcbasbdcxkopaSBXPKCJANQSDFJBASKJBDFKASJBDPKFJBASDKJBFAPKSJDBFKLASDJBFLKASJDBF')
>>> ca3=Category.objects.get(id=2)
>>> p3.category.add(ca3)

>>> User.objects.create_user('comm_boy1')
>>> User.objects.create_user('comm_boy2')
>>> User.objects.create_user('comm_girl1')
>>> User.objects.create_user('comm_girl2')

>>> comm_1=Comment.objects.create(post=Post.objects.get(id=1), author=User.objects.get(username='comm_boy1'), comment_text='Да не может быть')
>>> comm_2=Comment.objects.create(post=Post.objects.get(id=2), author=User.objects.get(username='comm_boy2'), comment_text='Зачем я продал неделю назад(')
>>> comm_3=Comment.objects.create(post=Post.objects.get(id=3), author=User.objects.get(username='comm_girl1'), comment_text='Странный текст статьи...')
>>> comm_4=Comment.objects.create(post=Post.objects.get(id=1), author=User.objects.get(username='comm_girl2'), comment_text='Кипр чемпион!')

>>> Post.like(Post.objects.get(id=1))
>>> Post.like(Post.objects.get(id=1))
>>> Post.like(Post.objects.get(id=1))

>>> Post.dislike(Post.objects.get(id=2))
>>> Post.dislike(Post.objects.get(id=2))

>>> Post.like(Post.objects.get(id=3))
>>> Post.like(Post.objects.get(id=3))
>>> Post.like(Post.objects.get(id=3))
>>> Post.like(Post.objects.get(id=3))

>>> Comment.like(Comment.objects.get(id=1))
>>> Comment.dislike(Comment.objects.get(id=2))
>>> Comment.dislike(Comment.objects.get(id=2))
>>> Comment.like(Comment.objects.get(id=3))
>>> Comment.like(Comment.objects.get(id=3))
>>> Comment.like(Comment.objects.get(id=3))
>>> Comment.dislike(Comment.objects.get(id=4))
>>> Comment.dislike(Comment.objects.get(id=4))
>>> Comment.dislike(Comment.objects.get(id=4))


>> Author.update_rating(Author.objects.get(id=1))
>>> Author.update_rating(Author.objects.get(id=2))




