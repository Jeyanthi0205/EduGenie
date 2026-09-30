from summary_module import summarize_text


text = """
Python is a high-level programming language known for its simple
and readable syntax. It is widely used in web development, data
science, artificial intelligence, automation, and software development.
Python supports multiple programming paradigms, including procedural,
object-oriented, and functional programming.
"""

summary = summarize_text(text)

print("SUMMARY TEST SUCCESSFUL!")
print()
print("Original text:")
print(text)
print()
print("Summary:")
print(summary)