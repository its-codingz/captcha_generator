import random
from captcha.image import ImageCaptcha

lower = "abcdefghijklmnoparstuvwxyz"
upper = "ABCDEFGHIJKLMNOPORSTUVNXYZ"
numbers = "0123456789"

mix = lower + upper + numbers
length = random.randrange(5,8)
random_Captcha = "".join(random.sample(mix, length))

image = ImageCaptcha(width = 280, height = 100)

captcha_text = random_Captcha
data = image.generate(captcha_text)

image.write(captcha_text,'CAPTCHA.png')
