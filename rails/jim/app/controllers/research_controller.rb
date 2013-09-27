class ResearchController < ApplicationController
  def index
    @papers = Paper.all
  end
end
