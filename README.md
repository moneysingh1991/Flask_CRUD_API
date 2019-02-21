# Flask_CRUD_API
To run this project virtual Environment and python is required 

1: Create table in MYSQL

run this query CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

2: Unzip flask-app.zip
3. Go to line 17 in main.py (change mysql credential)
3. go to terminal and run following commands
     cd task-app
     source venv/bin/activate                         (to activate virtual environment)
     python main.py
4. Go to url localhost:5000     
