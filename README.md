<div align="center">

# 📝 my_memo_app
  
This memo application was created using Django.

It allows you to create, view, edit, and delete memos.

<img src="https://github.com/mitamam/my_memo_app/assets/82627076/e1b6a156-b8dc-48c0-884e-20150316e18e" width="560px">

  
</div>

## ✨ How to use
required: `Git`, `Python3`

```shell
# clone this repository on your pc
git clone https://github.com/mitamam/my_memo_app.git
cd my_memo_app/

pip install -r requirements.txt

# generate SECRET_KEY
./gen_key.sh

python manage.py migrate
python manage.py runserver
```

### 🐳 Docker way
required: `Git`, `Docker`

```shell
# clone this repository on your pc
git clone https://github.com/mitamam/my_memo_app.git
cd my_memo_app/
  
docker compose up
```

