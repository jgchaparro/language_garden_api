# Create .venv

# Wrap into zip file

```python
Compress-Archive .\.venv\Lib\site-packages\* aws_lambda.zip
```

# Add main into the .zip
    
```python
Compress-Archive .\main.py -Update aws_lambda.zip
```


