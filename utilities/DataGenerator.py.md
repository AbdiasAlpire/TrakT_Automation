## Unique Data Generator Documentation 

### Table of Contents 
  * [Class: UniqueDataGenerator](#class-uniquedatagenerator)
    * [Constructor: `__init__`](#constructor-init)
    * [Method: `generate_unique_movie_comment`](#method-generate_unique_movie_comment)

### Class: UniqueDataGenerator 
 
This class is responsible for generating unique movie comments using the Faker library. 

* It ensures that each generated comment is at least 5 words long and has not been previously generated. 
* The generated comments are stored in a dictionary for tracking and preventing duplication.

#### Constructor: `__init__`

This method initializes the UniqueDataGenerator object.

**Parameters:**

* None

**Returns:**

* None

**Code:**

```python
    def __init__(self):
        self.faker = Faker()
        self.generated_data = {
            "movie_comment": []
        }
```

#### Method: `generate_unique_movie_comment`

This method generates a unique movie comment. 

**Parameters:**

* None

**Returns:**

* `str`: A unique movie comment string

**Code:**

```python
    def generate_unique_movie_comment(self):
        comment = self.faker.text()
        while len(comment.split()) < 5 or comment in self.generated_data["movie_comment"]:
            comment = self.faker.text()
        self.generated_data["movie_comment"].append(comment)
        return comment
```
