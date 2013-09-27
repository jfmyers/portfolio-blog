class CommentsController < ApplicationController
  def create
    @post = Post. find_by_slug(params[:post_id])
    #@post = Post.find(params[:post_id])
    @comment = @post.comments.create(params[:comment].permit(:commenter, :email, :body))
    redirect_to post_path(@post)
  end
  
end
