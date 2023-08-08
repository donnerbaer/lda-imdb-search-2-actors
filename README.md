[Youtube Video](https://www.youtube.com/watch?v=LDzkWtfUPyY)



# Einrichten

    pip install requests
    pip install bottle



# Workflow

1. download files to
    
	data/download/
	
2. unzip files to
    
	data/unzpped/
	
3. transform.py or transform_created_by_year.py
    
	data/transformed
	
4. import `.ttl`-files to graphDB
	
5. set login data in www/app.py
	
	endpoint_url
	username
	password

6. start service www/app.py

    http://localhost:80



