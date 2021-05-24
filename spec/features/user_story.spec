require 'rails_helper'

RSpec.describe 'User Story' do
 it "visit '/'
    fill in the search form with 'sweet potatoes'
    (Note: Use the existing search form)
    click 'Search'
    should be on page '/foods'
    should see a total of the number of items returned by the search.
    (sweet potatoes should find more than 30,000 results)
    should see a list of TEN foods that contain the ingredient 'sweet potatoes'
    For each of the foods I should see:
      - The food's GTIN/UPC code
      - The food's description
      - The food's Brand Owner
      - The food's ingredients " do

 end
end
