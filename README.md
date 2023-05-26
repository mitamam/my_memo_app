# my_memo_app

<img src="https://github.com/mitamam/my_memo_app/assets/82627076/252ba3cc-4485-4340-9416-712397048d0b" width="560px">

This is a memo application created for learning Django.

## Usage
```shell
git clone https://github.com/mitamam/my_memo_app.git
cd my_memo_app/

pip install -r requirements.txt

# Generate SECRET_KEY
n=$(python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
echo SECRET_KEY=$n > .env

python manage.py migrate
python manage.py runserver
```
