class Post < ActiveRecord::Base
  extend FriendlyId
  friendly_id :title, use: [:slugged, :history]
  #has_friendly_id :title, :use_slug => true
  #def to_param
  #  "#{id} #{title}".parameterize
  #end
  has_many :comments, dependent: :destroy
  validates :title, presence: true, length: {minimum: 5}
end