class CreateProjects < ActiveRecord::Migration
  def change
    create_table :projects do |t|
      t.text :descr
      t.string :title
      t.string :link

      t.timestamps
    end
  end
end
