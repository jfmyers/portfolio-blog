class CreateAbouts < ActiveRecord::Migration
  def change
    create_table :abouts do |t|
      t.text :about
      t.string :city
      t.string :company
      t.string :company_site
      t.string :company_site
      t.string :email
      t.string :fname
      t.string :github
      t.text :languages
      t.string :linkedin
      t.string :lname
      t.string :major
      t.string :minor
      t.string :site1_name
      t.string :site1_url
      t.string :site2_name
      t.string :site2_url
      t.string :site3_name
      t.string :site3_url
      t.text :skills
      t.string :state
      t.text :technologies
      t.string :title
      t.string :twitter

      t.timestamps
    end
  end
end
