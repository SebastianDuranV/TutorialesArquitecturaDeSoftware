from flask import Flask, redirect, render_template, url_for, request, flash
from consultor_sql import User, Category ,Post, db

app = Flask(__name__)
db.create_all()

TipeClass = dict(
    User = User,
    Category = Category,
    Post = Post
)

# Inicio
@app.route('/')
def index():
    return render_template('index.html')






#Crear
@app.route('/addUser')
def add_user():
    return render_template('create_user.html')

@app.route('/addCategory')
def add_category():
    return render_template('create_category.html')

@app.route('/addPost')
def add_post():
    return render_template('create_post.html')

@app.route('/createUser', methods = ['POST','GET'] )
def createUser():
    if request.method == 'POST':
        userName = request.form['username']
        email = request.form['email']
        user = User(username=userName , email=email)
        db.session.add(user)
        db.session.commit()
        #flash("User fue añadido")
        return redirect(url_for('add_user'))
    else:
        return redirect(url_for('add_user'))

@app.route('/createCategory', methods = ['POST','GET'] )
def createCategory():
    if request.method == 'POST':
        name = request.form['name']
        cat = Category(name=name)
        db.session.add(cat)
        db.session.commit()
        #flash("User fue añadido")
        return redirect(url_for('add_category'))
    else:
        return redirect(url_for('add_category'))

@app.route('/createPost', methods = ['POST','GET'] )
def createPost():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        idcategory = request.form['idcategory']
        iduser = request.form['iduser']
        category = Category.query.filter_by(id=idcategory).first_or_404()
        user = User.query.filter_by(id=iduser).first_or_404()
        post = Post(title=title , body=body,category=category, user=user)
        db.session.add(post)
        db.session.commit()
        #flash("User fue añadido")
        return redirect(url_for('add_post'))
    else:
        return redirect(url_for('add_post'))










# Eliminar
@app.route('/deleteUser/<username>')
def delete_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/deleteCategory/<idCat>')
def delete_category(idCat):
    cat = Category.query.filter_by(id=idCat).first_or_404()
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/deletePost/<idPost>')
def delete_post(idPost):
    post = Post.query.filter_by(id=idPost).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))









# Actualizar 
@app.route('/upUser/<username>')
def up_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('update_user.html' , user=user, username=username)

@app.route('/upCategory/<idCat>')
def up_category(idCat):
    cat = Category.query.filter_by(id=idCat).first_or_404()
    return render_template('update_category.html', cat=cat, id=idCat)

@app.route('/upPost/<idPost>')
def up_post(idPost):
    post = Post.query.filter_by(id=idPost).first_or_404()
    return render_template('update_post.html', post=post, id=idPost)


@app.route('/updateUser/<username>', methods = ['POST'] )
def updateUser(username):
    if request.method == 'POST':
        user = User.query.filter_by(username=username).first_or_404()
        user.userName = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        #flash("User fue añadido")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/updateCategory/<idCat>', methods = ['POST'] )
def updateCategory(idCat):
    if request.method == 'POST':
        cat = Category.query.filter_by(id=idCat).first_or_404()
        cat.name = request.form['name']
        db.session.commit()
        #flash("User fue añadido")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/updatePost/<idPost>', methods = ['POST'] )
def updatePost(idPost):
    if request.method == 'POST':
        post = Post.query.filter_by(id=idPost).first_or_404()
        post.title = request.form['title']
        post.body = request.form['body']
        post.category_id = request.form['idcategory']
        post.user_id = request.form['iduser']
        db.session.commit()
        #flash("User fue añadido")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))








# Mostrar
@app.route('/getList')
def getList():
    getObject = request.args.get('type','<h1> No type declarated </h1>')
    try:
        allObject = TipeClass[getObject].query.all()
    except:
        return '<h1> No found type </h1>'
    return render_template('show_list_types.html', objects=allObject , type=getObject)


@app.route('/user/<username>')
def show_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_user.html', user=user)


@app.route('/post/<idpost>')
def show_post(idpost):
    post = Post.query.filter_by(id=idpost).first_or_404()
    return render_template('show_post.html', post=post)

# Para despues::::::::::::::::
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#    else:
#        return show_the_login_form()


if __name__=='__main__':
    app.run(debug=True,port=8000)



