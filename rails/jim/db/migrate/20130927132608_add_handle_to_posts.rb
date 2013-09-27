class AddHandleToPosts < ActiveRecord::Migration
  def change
    add_column :posts, :handle, :string
    add_column :posts, :preview, :text
  end
end
