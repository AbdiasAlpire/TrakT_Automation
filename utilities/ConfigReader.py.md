##  Configuration Reader Documentation 📚

### Table of Contents 📑

* [Configuration Reader Overview](#configuration-reader-overview)
* [Usage](#usage)
* [Example](#example)

### Configuration Reader Overview

This code snippet provides a function to read configuration values from a `.ini` file. It leverages the `ConfigParser` module from the Python standard library. 

### Usage

The `read_configuration` function accepts two arguments:

| Argument | Type | Description |
|---|---|---|
| `category` | String | The name of the category within the `.ini` file. |
| `key` | String | The name of the key within the specified category. |

The function returns the value associated with the specified key within the given category.

### Example 

```python
# Import the function from the code snippet
from code_snippet import read_configuration

# Read the value associated with the "database" category and "host" key
database_host = read_configuration("database", "host")

# Print the value
print(f"Database host: {database_host}")
```

This example assumes a `config.ini` file with the following structure:

```ini
[database]
host = localhost
port = 3306
```

Running this code will print:

```
Database host: localhost
``` 
