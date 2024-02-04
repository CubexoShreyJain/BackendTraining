import psycopg2

cur = None

def show(query):
    
    cur.execute(query)
    res = cur.fetchall()
    print(res)
    print()

def run(query):
    
    cur.execute(query)


if __name__ == '__main__':
    conn = psycopg2.connect(database="cubexo", user = "cubexo", password = "shrey123", host = "127.0.0.1", port = "5432")
    curTemp = conn.cursor()
    cur = curTemp
    
    
# cur.execute("""
#             CREATE TABLE COURSES(course_id SERIAL PRIMARY KEY, course_name VARCHAR(50) UNIQUE NOT NULL, 
#             instructor VARCHAR(100) NOT NULL, topic VARCHAR(20) NOT NULL)
#             """)


# cur.execute("INSERT INTO COURSES(course_name, instructor, topic) VALUES('Introduction to SQL','Izzy Weber','Julia')");

# cur.execute("INSERT INTO COURSES(course_name, instructor, topic) VALUES('Analyzing Survey Data in Python','EbunOluwa Andrew','Python')");

# cur.execute("INSERT INTO COURSES(course_name, instructor, topic) VALUES('Introduction to ChatGPT','James Chapman','Theory')");

# cur.execute("INSERT INTO COURSES(course_name, instructor, topic) VALUES('Introduction to Statistics in R','Maggie Matsui','R')");

# cur.execute("INSERT INTO COURSES(course_name, instructor, topic) VALUES('Hypothesis Testing in Python','James Chapman','Python')");

# cur.execute("update COURSES SET topic = 'SQL' where course_id = 6;")


    show("SELECT * from COURSES;")

    run("drop table COURSES;")
    show("SELECT * from COURSES;")

    show("SELECT course_name from COURSES order by topic;") 

    show("SELECT course_name from COURSES order by topic;") 

    show('select instructor, topic from courses;')

    #counts the number of instructor with common topic
    show("SELECT topic, count(instructor) from COURSES group by topic;") 

    conn.commit()
    cur.close()
    conn.close()
    
    print("Database Closed!")
