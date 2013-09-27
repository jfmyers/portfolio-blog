class CreatePapers < ActiveRecord::Migration
  def change
    create_table :papers do |t|
      t.string :authors
      t.text :descr
      t.text :keywords
      t.text :news
      t.text :awards
      t.string :link

      t.timestamps
    end
  end
end
