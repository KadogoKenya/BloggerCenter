from flask import render_template, request, redirect, url_for,abort,flash
from . import main
from .. models import blogposts, Comment, User
from ..requests import get_quotes
from .. import db, photos
from flask_login import login_user,current_user,login_required,logout_user
from .forms import BlogpostForm, CommentForm,UpdateProfile

@main.route('/')
@main.route('/home')
def index():
    quotes = get_quotes()
    blogs = blogposts.query.all()
    return render_template('index.html',quotes=quotes,  blogs=blogs[::-1])




@main.route("/newblog", methods=['GET', 'POST'])
@login_required
def new_post():
    form = BlogpostForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content=form.content.data) 
        db.session.add(blog)
        db.session.commit()
        flash('Your blog has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('blogpost.html', title= 'new Blogpost', form=form, legend='Update blog')

@main.route("/post/<int:post_id>")
def blog(post_id):
    blog = blogposts.query.get_or_404(post_id)
    return render_template('post.html',title=blog.title, blog=blog)



@main.route("/blog/<int:blog_id>/update", methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = blogposts.query.get_or_404(blog_id)
   
    form= BlogpostForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash('Your blog has been updated!','success')
        return redirect(url_for('main.blog',post_id=blog.id))
    elif request.method =='GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('blogpost.html', title= 'Update blog', form=form, legend='Update blog', )



@main.route("/blog/<int:blog_id>/delete", methods=['GET','POST'])
@login_required
def delete_blog(blog_id):
    blog = blogposts.query.get_or_404(blog_id)
    if blog_id == current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash('Your blog has been deleted!', 'success')
    return redirect(url_for('main.index'))

@main.route('/new/comment/<int:post_id>',methods=['GET','POST'])
@login_required
def new_comment(post_id):
    form=CommentForm()
    if form.validate_on_submit():
        description = form.description.data
        new_comment=Comment(description=description,user_id=current_user._get_current_object().id, post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.new_comment',form = form,post_id=post_id))
    all_comments = Comment.query.filter_by(blogpost_id=post_id).all()
    return render_template('comments.html',form=form,comments=all_comments,post_id=post_id)

@main.route('/deleteComment/<int:comment_id>/<int:blog_id>', methods=["GET", "POST"])
def delete_Comment(comment_id, post_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.new_blog", id=blog_id,post_id=post_id))

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route('/update',methods = ['GET','POST'])
@login_required
def update_profile():
    current_user = User.query.filter_by(username = current_user).first()
    if current_user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        current_user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile'))

    return render_template('update_profile.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))
