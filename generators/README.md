# Generators
i.e. code that generates other code! 

## generate_default_values
Quick script that parses a YAML file of LED specs and tries to come up with a normalizing array such that the brightness are the same. 

Emphasis on _tries_.
At present it assumes brightness scales with current (it does not) and that humans percieve all colors the same (we do not). 
But hey, it gets 95% of the way there, so that's good enough. 
