class Comment < ActiveRecord::Base
  belongs_to :post
  validates :commenter , presence: true, length:{minimum: 2} 
  validates :email , presence: true, length:{maximum: 30} 
  validates_format_of :email, :with => /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\z/i
  validates :body , presence: true
end
