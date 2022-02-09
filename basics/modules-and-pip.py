# Import files with `import <filename>` keyword
import tuples

print(tuples.monthYear)

# Install packages with pip install <package>
# To create a file of packages that allows for repeatable builds it's common to use a requirements.txt file which can be created using: pip freeze > requirements.txt
# We can then install the packages by their pinned version from freeze: pip install -r requirements.txt