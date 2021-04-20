import pymysql
db = pymysql.connect(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db = 'busan'
)
sql = '''
  CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
sql_1 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네 ㅠㅠ', '김태경');"
sql_2 = "INSERT INTO `users` (`name`, `email`, `username`, `password`) VALUES ('최형욱', 'wookdersar@naver.com', 'CHOI', '12345');"
sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"

title = input('제목을 적으세요')
body = input("내용을 적으세요")
author = input("누구세요?")

input_data = [title,body,author ]
cursor = db.cursor()
cursor.execute(sql_3,input_data)
db.commit()
db.close()

# cursor = db.cursor()

# cursor.execute(sql)
# cursor.execute(sql_1)

# cursor.execute(sql_2)

# db.commit()
# db.close()

# cursor.execute('SELECT * FROM users;')
# cursor.execute('SELECT * FROM topic;')
# users = cursor.fetchall()
# print(users)