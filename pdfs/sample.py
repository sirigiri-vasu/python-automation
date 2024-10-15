import fitz

import fitz  # PyMuPDF
import json

def create_pdf_from_json(json_data, output_filename):
    # Create a PDF document
    pdf_document = fitz.open()
    
    # Add a new page
    page = pdf_document.new_page()
    
    # Load JSON data
    data = json.loads(json_data)
    
    # Define the starting position for adding content
    x_position = 50
    y_position = 50
    
    # Add content to the PDF from JSON data
    page.insert_text((x_position, y_position), "Items Information", fontsize=14)
    y_position += 30  # Move down after the title
    
    for item in data['items']:
        content = f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}"
        page.insert_text((x_position, y_position), content)
        y_position += 20  # Move to the next line
    
    # Save the PDF document
    pdf_document.save(output_filename)
    pdf_document.close()

# Sample JSON data
json_data = '''
{
  "items": [
    {
      "name": "Item 1",
      "price": 10,
      "quantity": 5
    },
    {
      "name": "Item 2",
      "price": 20,
      "quantity": 3
    },
    {
      "name": "Item 3",
      "price": 15,
      "quantity": 7
    }
  ]
}
'''

# Create a PDF from the JSON data
create_pdf_from_json(json_data, "items_information.pdf")

