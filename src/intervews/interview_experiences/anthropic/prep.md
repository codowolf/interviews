# Coding
## Duplicates
### Options
#### Option 1 — based on size
- Not really reliable and multiple files can have same size

#### Option 2 — 1 + filename and size
- Not reliable as multiple files can have same name or size

#### Option 3 — Full Hash of File
- Solves the duplicate issue, but have to load entire file in-memory to hash
- Not scalable

#### Option 4 — Multi-Hash of File
- Solves the issue in scalable way
- Does not load entire file into memory
- Chunk size allows flexible way to create hashes
- Scales indefinitely
```python
# MULTI HASH
def get_multi_hash(path):  
    """  
    Given a path to a file, returns multiple hashes based on chunk size.    
    - Ensure that file is opened in binary mode = "rb"  
    - Ensure file size is retrieved by os.path.getsize    
    - Ensure if file chunk is not read, return    
    """    
    hashes = []  
    fsize = os.path.getsize(path)  
    chunk_size = 100  
    with open(path, 'rb') as f:  
        ptr = 0  
        while ptr < fsize:  
            f.seek(ptr)  
            chunk = f.read(chunk_size)  
            if not chunk:  
                break  
            hashes.append(hashlib.sha256(chunk).hexdigest())  
            ptr += chunk_size  
  
    return hashes
```

- Given a folder, iterate through all files
```python
def get_all_files(path):  
    for dirpath, dirnames, filenames in os.walk(path):  
        for filename in filenames:  
            yield os.path.join(dirpath, filename)
# Yields file names, followed by visiting dirs, then file names. 
# Essentially DFS
"""
/Users/nodofox/Documents/GitHub/interviews/src ['intervews'] ['main.java']
/Users/nodofox/Documents/GitHub/interviews/src/intervews ['interview_experiences', 'self'] []
/Users/nodofox/Documents/GitHub/interviews/src/intervews/interview_experiences ['uber', 'databricks', 'rh', 'perplexity', 'dd', 'anthropic', 'affirm'] ['tiktok.md', 'maven.md']
/Users/nodofox/Documents/GitHub/interviews/src/intervews/interview_experiences/uber [] ['interview.md']
/Users/nodofox/Documents/GitHub/interviews/src/intervews/interview_experiences/databricks ['prep'] ['interview.md']
/Users/nodofox/Documents/GitHub/interviews/src/intervews/interview_experiences/databricks/prep ['coding'] ['test.py']
"""
```

- Convert  a list to a tuple = `my_tuple = tuple(my_list)`


