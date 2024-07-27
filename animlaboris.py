class Field:
    def __init__(self):
        self.content = "Some text"

field = Field()

# Reset the content to an empty string
field.content = ""

print(f"Field content: '{field.content}'")  # Output: Field content: ''
